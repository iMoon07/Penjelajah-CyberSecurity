# SQL Injection — PortSwigger Web Security Academy

[🇬🇧 Read in English](sql-injection-en.md)

﷽

## What is that?

![sql-injection](sql-injection.png)

This learning path introduces SQL injection (SQLi), a critical web vulnerability. You'll learn how to detect and exploit SQLi to uncover hidden data and manipulate application behavior, as well as essential techniques to secure applications against SQLi attacks.

## What is SQL injection (SQLi)?
### Resume

## How to detect SQL injection vulnerabilities
### SQL injection in different parts of the query

## Retrieving hidden data
### Retrieving hidden data - Continued
#### Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

## Subverting application logic
#### Lab: SQL injection vulnerability allowing login bypass

## SQL injection UNION attacks
### SQL injection UNION attacks - Continued
### Determining the number of columns required
#### Determining the number of columns required
#### Determining the number of columns required - Continued
##### Lab: SQL injection UNION attack, determining the number of columns returned by the query
#### Database-specific syntax
### Finding columns with a useful data type
#### Finding columns with a useful data type
##### Lab: SQL injection UNION attack, finding a column containing text
### Using a SQL injection UNION attack to retrieve interesting data
#### Using a SQL injection UNION attack to retrieve interesting data
##### Lab: SQL injection UNION attack, retrieving data from other tables
### Retrieting multiple values within a single column
#### Retrieting multiple values within a single column
##### Lab: SQL injection UNION attack, retrieving multiple values in a single column

## Examining the database
### Examining the database in SQL injection attacks
#### Querying the database type and version
##### Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft
#### Listing the contents of the database
##### Lab: SQL injection attack, listing the database contents on non-Oracle databases

## Blind SQL injection
### What is blind SQL injection?
### Exploiting blind SQL injection by triggering conditional responses
#### Exploiting blind SQL injection by triggering conditional responses
#### Exploiting blind SQL injection by triggering conditional responses - Continued
##### Lab: Blind SQL injection with conditional responses

## Error-based SQL injection
#### Exploiting blind SQL injection by triggering conditional errors
#### Exploiting blind SQL injection by triggering conditional errors - Continued
##### Lab: Blind SQL injection with conditional errors
#### Extracting sensitive data via verbose SQL error messages
#### Extracting sensitive data via verbose SQL error messages - Continued
##### Lab: Visible error-based SQL injection
### Exploiting blind SQL injection by triggering time delays
#### Exploiting blind SQL injection by triggering time delays
#### Exploiting blind SQL injection by triggering time delays - Continued
##### Lab: Blind SQL injection with time delays and information retrieval
### Exploiting blind SQL injection using out-of-band (OAST) techniques
#### Exploiting blind SQL injection using out-of-band (OAST) techniques
#### Exploiting blind SQL injection using out-of-band (OAST) techniques - Continued
##### Lab: Blind SQL injection with out-of-band interaction
#### Exploiting blind SQL injection using out-of-band (OAST) techniques - Continued
##### Lab: Blind SQL injection with out-of-band data exfiltration

## SQL injection in different contexts
#### Lab: SQL injection with filter bypass via XML encoding

## Second-order SQL injection

## How to prevent SQL injection
### How to prevent SQL injection - Continued