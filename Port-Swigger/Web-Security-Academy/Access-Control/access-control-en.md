# Access Control — PortSwigger Web Security Academy

[🇮🇩 Read in Bahasa Indonesia](access-control-id.md)

﷽

## What is access control?

![access-control](images/overview/access-control.png)

What is access control?
Access control is the application of constraints on who or what is authorized to perform actions or access resources. In the context of web applications, access control is dependent on authentication and session management:

- **Authentication** confirms that the user is who they say they are.
- **Session management** identifies which subsequent HTTP requests are being made by that same user.
- **Access control** determines whether the user is allowed to carry out the action that they are attempting to perform.

Broken access controls are common and often present a critical security vulnerability. Design and management of access controls is a complex and dynamic problem that applies business, organizational, and legal constraints to a technical implementation. Access control design decisions have to be made by humans so the potential for errors is high.

### Access control security models

In this section we explain what access control security models are and we discuss the most commonly encountered models.

### What are access control security models?

An access control security model is a formally defined definition of a set of access control rules that is independent of technology or implementation platform. Access control security models are implemented within operating systems, networks, database management systems and back office, application and web server software. Various access control security models have been devised over the years to match access control policies to business or organizational rules and changes in technology.

### Programmatic access control

With programmatic access control, a matrix of user privileges is stored in a database similar and access controls are applied programmatically with reference to this matrix. This approach to access control can include roles or groups or individual users, collections or workflows of processes and can be highly granular.

### Discretionary access control (DAC)

With discretionary access control, access to resources or functions is constrained based upon users or names groups of users. Owners of resources or functions have the ability to asign or delegate access permissions to users. This model is highly granular with access rights defined to an individual resource or function and user. Consequently the model can become very complex to design and manage.

### Mandatory access control (MAC)

Mandatory access control is a centrally controlled system of access control in which access to some object (a file or other resource) by a subject is constrained. Significantly, unlike DAC the users and owners of resources have no capability to delegate or modify access rights for their resources. This model is often associated with military clearance-based systems.

### Role-based access control (RBAC)

With role-based access control, named roles are defined to which access control privileges are assigned. Users are then assigned to single or multiple roles. RBAC provides enhanced management over other access control models and if properly designed sufficient granularity to provide manageable access control in complex applications. For example, the purchase clerk might be defined as a role with access permissions for a subset of purchases clerk role. RBAC is most effective when ther are sufficient roles to properly invoke access controls but not so many as to make the model excessively complex and unwieldy to manage.

### Vertical access controls

Vertical access controls are mechanisms that restrict access to sensitive functionality to specific types of users.

With vertical access controls, different types of users have access to different application functions. For example, an administrator might be able to modify or delete any user's account, while an ordinary user has no access to these actions. Vertical access controls can be more fine-grained implementations of security models designed to enforce business policies such as separation of duties and least privilege.

### Horizontal access controls

Horizontal access controls are mechanisms that restrict to resources to specific users.

With horizontal access controls, different users have access to a subset of resources of the same type. For example, a banking application will allow a user to view transactions and make payments from their own accounts, but not accounts of any other user.

### Context-dependent access controls

Context-dependent access control restrict access to functionality and resources based upon the state of the application or the user's interaction with it.

Context-dependent access controls prevent a user performing actions in the wrong order. For example, a retail website might prevent users from modifying the contents of their shopping cart after they have made payment.

## Examples of broken access controls

Broken access control vulnerabilities exist when a user can access resources or perform actions that they are not supposed to be able to.

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

## How to prevent access control vulnerabilities