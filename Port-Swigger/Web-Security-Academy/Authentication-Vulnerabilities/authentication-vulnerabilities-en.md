# Authentication Vulnerabilities — PortSwigger Web Security Academy

[🇮🇩 Read in Bahasa Indonesia](authentication-vulnerabilities-id.md)

﷽

## What is that?

![authentication-vulnerabilities](images/overview/authentication-vulnerabilities.png)

## What is authentication?

## What is the difference between authentication and authorization?

## How do authentication vulnerabilities arise?

## What is the impact of vulnerable authentication?

## Vulnerabilities in password-based login

### Brute-force attacks

### Brute-forcing usernames

### Brute-forcing passwords

### Username enumeration

##### Lab: Username enumeration via different responses

##### Lab: Username enumeration via subtly different responses

##### Lab: Username enumeration via response timing

### Flawed brute-force protection

##### Lab: Broken brute-force protection, IP block

### Account locking

##### Lab: Username enumeration via account lock

### User rate limiting

### HTTP basic authentication

## Vulnerabilities in multi-factor authentication

### Two-factor authentication tokens

### Bypassing two-factor authentication

##### Lab: 2FA simple bypass

### Flawed two-factor verification logic

##### Lab: 2FA broken logic

### Brute-forcing 2FA verification codes

## Vulnerabilities in other authentication mechanisms

### Keeping users logged in

##### Lab: Brute-forcing a stay-logged-in cookie

##### Lab: Offline password cracking

### Resetting user passwords

### Sending passwords by email

### Resetting passwords using a URL

##### Lab: Password reset broken logic

##### Lab: Password reset poisoning via middleware

### Changing user passwords

##### Lab: Password brute-force via password change

## Preventing attacks on your own authentication mechanisms
