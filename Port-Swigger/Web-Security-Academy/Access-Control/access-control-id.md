# Access Control — PortSwigger Web Security Academy

[🇬🇧 Read in English](access-control-en.md)

﷽

## Apa itu access control?

![access-control](images/overview/access-control.png)

## Model keamanan access control

### Vertical access controls

### Horizontal access controls

### Context-dependent access controls

## Contoh broken access controls

### Vertical privilege escalation

#### Unprotected functionality

##### Lab: Unprotected admin functionality

##### Lab: Unprotected admin functionality with unpredictable URL

#### Parameter-based access control methods

##### Lab: User role controlled by request parameter

##### Lab: User role can be modified in user profile

#### Broken access control resulting from platform misconfiguration

##### Lab: URL-based access control can be circumvented

##### Lab: Method-based access control can be circumvented

#### Broken access control resulting from URL-matching discrepancies

### Horizontal privilege escalation

##### Lab: User ID controlled by request parameter

##### Lab: User ID controlled by request parameter, with unpredictable user IDs

##### Lab: User ID controlled by request parameter with data leakage in redirect

#### Horizontal to vertical privilege escalation

##### Lab: User ID controlled by request parameter with password disclosure

### Insecure direct object references

##### Lab: Insecure direct object references

### Access control vulnerabilities in multi-step processes

##### Lab: Multi-step process with no access control on one step

### Referer-based access control

##### Lab: Referer-based access control

### Location-based access control

## Cara mencegah kerentanan access control