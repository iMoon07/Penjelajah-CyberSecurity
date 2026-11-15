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



### NoSQL Operator Injection

#### Submitting Query Operators

#### Detecting Operator Injection in MongoDB

##### Lab: Exploiting NoSQL Operator Injection to Bypass Authentication

### Exploiting Syntax Injection to Extract Data

#### Exfiltrating Data in MongoDB

#### Identifying Field Names

#### Identifying Field Names - Continued

##### Lab: Exploiting NoSQL Injection to Extract Data

### Exploiting NoSQL Operator Injection to Extract Data

#### Injecting Operators in MongoDB

#### Extracting Field Names

#### Exfiltrating Data Using Operators

##### Lab: Exploiting NoSQL Operator Injection to Extract Unknown Fields

### Timing Based Injection

#### Timing Based Injection

### Preventing NoSQL Injection

#### Prevention Strategies