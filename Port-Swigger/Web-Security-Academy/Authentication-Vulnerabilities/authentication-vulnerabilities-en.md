# Authentication Vulnerabilities — PortSwigger Web Security Academy

[🇮🇩 Read in Bahasa Indonesia](authentication-vulnerabilities-id.md)

﷽

## What is that?

![authentication-vulnerabilities](images/overview/authentication-vulnerabilities.png)

This learning path explores authentication vulnerabilities, which have a critical impact on security. You'll learn about common mechanisms and vulnerabilities, and strategies for robust authentication.

## What is authentication?

Conceptually, authentication vulnerabilities are easy to understand. However, they are usually critical because of the clear relationship between authentication and security.

Authentication vulnerabilities can allow attackers to gain access to sensitive data and functionality. They also expose additional attack surface for futher exploits. For this reason, it's important to learn how to identify and exploit authentication and exploit authentication vulnerabilities, and how to bypass common protection measures.

Authentication is the process of verifying the identity of user or client. Websites are potentially exposed to anyone who is connected to the internet. This makes robust authentication mechanisms integral to effective web security.

There are three main types of authentication:

- Something you *know*, such as a password or the answer to a security question. These are sometimes called "knowledge factors"
- Something you *have*, This is a physical object such as a mobile phone or security token. These are sometimes called "knowledge factors".
- Something you *are* or do. For example, you biometrics or patterns of behaviour. These are sometimes called "inherence factors".

Authentication mechanism rely on a range of technologies to verify one or more of these factors.

## What is the difference between authentication and authorization?

Authentication is the prosess of verifying that a user is who they claim to be. Authorization involves verifying whether a user is allowed to do something.

For example, authentication determines whether someone attempting to access a website with the username `Carlos123` really is the same person who created the account.

Once `Carlos123` is authenticated, their permissions determine what they are authorized to do. For example, they may be authorized to access personal information about other users, or perform actions such as deleting another user's account.

## How do authentication vulnerabilities arise?

Most vulnerabilities in authentication mechanisms occur in one of two ways:

- The authentication mechanism are weak because they fail to adequately protect agains brute-force attacks.
- Logic flaws or poor coding in the implementation allow the authentication mechanism to be bypassed entirely by an attacker. This is sometimes called "broken authentication".

In many areas of web development, logic flaws cause the website to behave unexpectedly, which may or may not be a security issue. However, as authentication is so crital to security, it's very likely that flawed authentication logic exposes the website to security issues.

## What is the impact of vulnerable authentication?

The impact of authentication vulnerabilities can be severe. If an attacker bypasses authentication or brute-forces their way into another user's account, they have access to all the data and functionality that the compromised account has. If they are able to compromise a high-privileged account, such as a system administrator, they could take full control over the entire application and potentially gain access to internal infrastructure.

## What is the impact of vulnerable authentication? - Continued

Even compromising a low-privileged account might still grant an attacker access to data that they otherwise shouldn't have, such as commercially sensitive business information. Even if the account does not have to access additional pages, which provide a futher attack surface. Often, high-severity attacks are not possible from publicly accessible pages, but they may be possible form an internal page.

## Vulnerabilities in password-based login

For websites that adopt a password-based login process, users either register for an account themselves or they are assigned an account by an administrator. This account is associated with a unique username and a secret password, which the user enters in a login form to authenticate themselves.

In this scenarion, the fact that they know the secret password is taken as sufficient proof of the user's identity. This means that the security of the website is compromised if an attacker is able to either obtain or guess the login credentials of another user.

This can be achieved in a number of ways. The following sections show how an attacker can use brute-force attacks, and some of the flaws in brute-force protection. You'll also learn about the vulnerabilities in HTTP basic authentication.

### Brute-force attacks

A brute-force attack is when an attacker uses a system of trial and error to guess valid user credentials. These attacks are typically automated using wordlists of usernames and passwords. Automating this process, especially using dedicated tools, potentially enables an attacker to make vast numbers of login attempts at high speed.

Brute-forcing is not always just a case of making completely random guesses at usernames and passwords. By also using basic logic or publicy available knowlege, attackers can fine-tune brute-force attacks to make much more educated guesses. This considerably increases the efficiency of such attacks. Websites that rely on password-based login as their sole method of authenticating users can be highly vulnerable if they do not implement sufficient brute-force protection.

### Brute-forcing usernames

Usernames are especially easy to guess if they conform to a recognizable pattern, such as an email address. For example, it is very common to see business logins in the format `firstname.lastname@somecompany.com`. However, even if there is no obvious pattern, sometimes even high-privileged accounts are created using predictable usernames, such as `admin` or `administrator`.

During auditing, check whether the website discloses potential usernames publicly. For example, are you able to access user profiles without logging in? Even if the actual content of the profiles is hidden, the name used in the profile is sometimes the same as the login username. You should also check HTTP responses to see if any email addresses are disclosed. Occasionally, responses contain email addresses of high-privileged users, such as administrator or IT support.

### Brute-forcing passwords

Passwords can similary be brute-forced, with the difficulty varying based on the strengh of the password. Many websites adopt some form of password policy, which forces users to create-high-entropy passwords that are, theoretically at least, harder to crack using brute-force alone. This typically involves enforcing passwords with:

- A minimum number of characters
- A mixture of lower and uppercase letters
- At least one special character

### Brute-forcing passwords - Contiuned

However, while high-entropy passwords are difficult for computers alone to crack, we can use a basic knowledge of human behaviour to exploit vulnerabilities

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
