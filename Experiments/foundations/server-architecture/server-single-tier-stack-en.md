# Server Single-Tier Stack: Understanding Components, Technologies, and Deployment

[🇮🇩 Baca dalam Bahasa Indonesia](server-single-tier-stack-id.md)
[🇲🇾 Baca dalam Bahasa Melayu](server-single-tier-stack-ms.md)
[🇵🇭 Basahin sa Tagalog](server-single-tier-stack-tl.md)

## One Server, One Stack

﷽

![Server Single-Tier Stack: Memahami Komponen, Teknologi, dan Deployment](single-tier-stack.png)

A **server single-tier stack** refers to an architecture in which the [web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), [application runtime](https://en.wikipedia.org/wiki/Runtime_system), and [database](https://en.wikipedia.org/wiki/Database) all run on a **single machine**.

Imagine a small eatery where the kitchen, dining area, and storage are all in one place. A customer places an order, the chef prepares it, and the meal is served on the spot. Everything takes place in the same location.

This concept is much like a **single-tier stack**: the core components of an application—namely the web server, application runtime, and database—are prepared together and served to the user, much like a meal being served from that kitchen.

But how does this work when a visitor accesses a website built on a single-tier stack?

## The Flow

```mermaid
flowchart TD
    C["🧑‍🦱 Customer<br/>Places an order"] -->|"1. Place order<br/>as HTTP Request"| P["🧑‍🍳 Waiter<br/>Takes the order and forwards it"]
    P -->|"2. Forward order<br/>to the kitchen"| K["👨‍🍳 Chef<br/>Prepares the order"]
    K -->|"3. Retrieve ingredients<br/>if needed"| G["🥫 Pantry<br/>Stores ingredients"]
    G -->|"4. Send ingredients<br/>to the chef"| K
    K -->|"5. Serve meal<br/>to the waiter"| P
    P -->|"6. Deliver meal<br/>to the customer<br/>as HTTP Response"| C

    subgraph W["Eatery / Single Location"]
        P
        K
        G
    end
```

## Core Components

| Component | Eatery Analogy | Function |
| --- | --- | --- |
| [Operating System (OS)](https://en.wikipedia.org/wiki/Operating_system) | The building itself | The foundation. Manages hardware, memory, processes, and server resources. |
| [Web Server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server) | The waiter | Receives HTTP/HTTPS requests, forwards them to the application, and returns the response to the client. |
| [Application Runtime](https://en.wikipedia.org/wiki/Runtime_system) | The chef | Executes application code so that the logic can be processed and turned into a ready-to-serve response. |
| [Database](https://en.wikipedia.org/wiki/Database) | The pantry/storage room | Stores, organizes, and retrieves the data required by the application. Not always needed if the application does not require persistent data storage. |

## Supporting Components

| Component | Eatery Analogy | Function |
| --- | --- | --- |
| [Web Client](https://en.wikipedia.org/wiki/Web_browser) | The customer | The user-side application (e.g., a web browser) that sends HTTP requests to the server and renders HTTP responses. |
| [TLS (Transport Layer Security) & TLS Certificate](https://en.wikipedia.org/wiki/Transport_Layer_Security) | Sealed packaging & official business license | Secures communication over HTTPS with encryption, server authentication, and data integrity. SSL is the deprecated predecessor of TLS. Certificates help browsers verify the server's identity. For public websites, HTTPS with TLS 1.2 or TLS 1.3 is considered the standard. |
| [Cache (optional)](https://en.wikipedia.org/wiki/Cache_(computing)) | Ready-to-serve items on display | Temporarily stores frequently accessed data to improve performance and reduce load on the server. |

> *Note:* Supporting components are not always required for an application to run. Their need depends on the application's purpose, the user experience desired, security requirements, and the deployment environment. Some may be nearly essential (e.g., HTTPS for public websites), while others are only added when they provide clear benefits (e.g., caching for performance).

Reference: [MDN — How the Web Works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)

## Technology Stack Combinations

```mermaid
flowchart TD
    A["🍜 Technology Stack<br/>= Recipe and ingredients"] --> B{"Choose ingredients based on the menu"}
    B --> C["🟨 JavaScript / TypeScript<br/>React, Node.js, MongoDB"]
    B --> D["🐘 PHP<br/>Laravel, LAMP, LEMP"]
    B --> E["🐍 Python<br/>Django, FastAPI, Flask"]
    B --> F["🔷 .NET<br/>ASP.NET Core, Blazor"]
    B --> G["☕ Java<br/>Spring Boot, Jakarta EE"]
    B --> H["💎 Ruby<br/>Ruby on Rails"]
    B --> I["🐹 Go<br/>Gin, Echo, Fiber"]
    B --> J["🦀 Rust<br/>Actix, Axum, Rocket"]
    B --> K["📊 Infrastructure<br/>ELK, Prometheus + Grafana"]
    C --> L["🍽️ Web Application / API<br/>tailored to project needs"]
    D --> L
    E --> L
    F --> L
    G --> L
    H --> L
    I --> L
    J --> L
    K --> L
```

A technology stack is akin to a recipe and its ingredients. In computing, the choice of operating system, web server, programming language, framework, and database forms a distinct arrangement known as a [solution stack](https://en.wikipedia.org/wiki/Solution_stack).

Each stack carries its own composition and purpose, tailored to the requirements of the application at hand. Below are some of the most widely used technology stacks, along with their components and use cases.

### 1. JavaScript & TypeScript Stack

This stack leverages JavaScript or TypeScript to build both the user interface (frontend) and server logic (backend). With Node.js, Bun, or Deno, JavaScript can run on the server, allowing a single language to cover the entire application stack.

| Stack | Core Components | Description |
| --- | --- | --- |
| [MEAN](https://www.mongodb.com/resources/languages/mean-stack) | [MongoDB](https://www.mongodb.com/), [Express.js](https://expressjs.com/), [Angular](https://angular.dev/), [Node.js](https://nodejs.org/) | Uses Angular for a SPA frontend, Express.js as the backend framework, Node.js as the runtime, and MongoDB as a NoSQL database. Well-suited for enterprise applications requiring a strong structure and built-in TypeScript support via Angular. |
| [MERN](https://www.mongodb.com/resources/languages/mern-stack) | [MongoDB](https://www.mongodb.com/), [Express.js](https://expressjs.com/), [React](https://react.dev/), [Node.js](https://nodejs.org/) | Uses React for a component-based frontend, Express.js for the API backend, Node.js as the runtime, and MongoDB as the database. Highly popular for modern web and mobile backends due to React's flexibility and the vast npm ecosystem. |
| [MEVN](https://www.mongodb.com/resources/languages/mern-stack) | [MongoDB](https://www.mongodb.com/), [Express.js](https://expressjs.com/), [Vue.js](https://vuejs.org/), [Node.js](https://nodejs.org/) | Uses Vue.js as a progressive frontend framework, Express.js for the backend, Node.js as the runtime, and MongoDB as the database. Known for its lightweight nature, ease of learning, and reactivity, making it well-suited to medium-scale applications. |
| [PERN](https://www.digitalocean.com/community/tutorials/how-to-build-a-pern-stack-application) | [PostgreSQL](https://www.postgresql.org/), [Express.js](https://expressjs.com/), [React](https://react.dev/), [Node.js](https://nodejs.org/) | Replaces MongoDB with PostgreSQL, a relational (ACID-compliant) database, while retaining React, Express.js, and Node.js. Ideal for applications that demand data integrity, complex queries, and strict relationships between tables. |
| [Next.js Stack](https://nextjs.org/) | [Next.js](https://nextjs.org/), [React](https://react.dev/), [Node.js](https://nodejs.org/), PostgreSQL or MySQL | A React framework supporting Server-Side Rendering (SSR), Static Site Generation (SSG), and API routes within a single project. Well-suited for SEO-driven applications, fast page loads, and full-stack development in a unified repository. |
| [T3 Stack](https://create.t3.gg/) | [TypeScript](https://www.typescriptlang.org/), [Tailwind CSS](https://tailwindcss.com/), [tRPC](https://trpc.io/), [Next.js](https://nextjs.org/), [Prisma](https://www.prisma.io/), [PostgreSQL](https://www.postgresql.org/) | A full-stack TypeScript stack that enforces end-to-end type safety from database to frontend. tRPC eliminates the need for manual REST APIs, Prisma provides a type-safe ORM, and Tailwind handles styling. Ideal for teams prioritizing type safety and rapid development. |
| [JAMstack](https://jamstack.org/what-is-jamstack/) | JavaScript, API, Markup | An architectural approach that decouples frontend markup from the backend. JavaScript runs on the client, data is fetched via APIs, and markup is pre-built at build time. Ideal for content sites, static e-commerce, and applications requiring high security and scalability without a traditional server. |
| [Bun Stack](https://bun.sh/) | [Bun](https://bun.sh/), [Elysia](https://elysiajs.com/) or [Hono](https://hono.dev/), SQLite or PostgreSQL, React or Vue | Uses Bun as a JavaScript runtime that replaces Node.js with faster startup and lower memory usage. Paired with lightweight frameworks like Elysia or Hono and a relational database. Suitable for microservices, serverless, and latency- or resource-sensitive applications. The ecosystem remains younger than Node.js. |

### 2. PHP Stack

A PHP-centric stack is commonly used for web development, typically run on the server alongside a web server and a relational database.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Laravel](https://laravel.com/) | [PHP](https://www.php.net/), [Laravel](https://laravel.com/docs), MySQL or PostgreSQL, Nginx or Apache | A modern PHP framework offering routing, authentication, Eloquent ORM, Blade templating, and more. Ideal for web applications ranging from small projects to large-scale systems, with extensive documentation and a structured approach to development. |
| [Symfony](https://symfony.com/) | [PHP](https://www.php.net/), [Symfony](https://symfony.com/doc/current/index.html), various databases, Nginx or Apache | A modular, reusable set of PHP components widely used as the foundation for many frameworks, including Laravel. Highly flexible and well-suited for large-scale enterprise applications that require full control over architecture. |
| [LAMP](https://cloud.google.com/mysql/lamp) | [Linux](https://www.kernel.org/), [Apache](https://httpd.apache.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | The classic stack for dynamic web applications. Linux serves as the OS, Apache as the web server, MySQL/MariaDB as the database, and PHP as the programming language. Widely supported by hosting providers and easy to deploy. |
| [LEMP](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-ubuntu-22-04) | [Linux](https://www.kernel.org/), [Nginx](https://nginx.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | A LAMP variant that replaces Apache with Nginx. Nginx is more efficient at handling concurrent connections and serving static content, making it ideal for high-traffic applications or those requiring greater web server performance. |
| [WAMP](https://en.wikipedia.org/wiki/WAMP) | [Windows](https://www.microsoft.com/windows), [Apache](https://httpd.apache.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | A Windows-based PHP stack designed for local development and hosting. Suitable for environments rooted in Microsoft infrastructure. |
| [WIMP](https://learn.microsoft.com/en-us/iis/) | [Windows](https://www.microsoft.com/windows), [IIS](https://www.iis.net/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | A Windows-based stack using IIS (Internet Information Services) in place of Apache. Well-suited for organizations integrated with the Microsoft ecosystem running PHP on Windows Server. |
| [FAMP](https://en.wikipedia.org/wiki/FAMP) | [FreeBSD](https://www.freebsd.org/), [Apache](https://httpd.apache.org/), [MySQL](https://mariadb.org/) or [MariaDB](https://mariadb.org/), [PHP](https://www.php.net/) | A LAMP variant using FreeBSD as the operating system. Known for its stability, security, and efficiency in networking, making it ideal for servers where OS robustness is a priority. |
| [XAMPP](https://www.apachefriends.org/) | Cross-platform, [Apache](https://httpd.apache.org/), [MariaDB](https://mariadb.org/) or [MySQL](https://mariadb.org/), [PHP](https://www.php.net/), [Perl](https://www.perl.org/) | An all-in-one, easy-to-install web development package for Windows, Linux, and macOS. Primarily used for learning and local prototyping before deployment to production. |

### 3. Python Stack

A Python-based stack for web development, ranging from micro-frameworks to full-stack frameworks rich with built-in functionality.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Django](https://www.djangoproject.com/) | [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), PostgreSQL or MySQL, Nginx or Apache, Gunicorn | A "batteries included" framework offering an admin panel, authentication, ORM, and robust security features out of the box. Ideal for large-scale web applications requiring rapid development and high security standards. |
| [FastAPI](https://fastapi.tiangolo.com/) | [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/), PostgreSQL or MySQL, Nginx, Uvicorn | A modern API framework with automatic data validation via Pydantic and interactive documentation through Swagger/OpenAPI. Highly performant with async support, making it ideal for microservices and machine learning APIs. |
| [Flask](https://flask.palletsprojects.com/) | [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/), various databases, Nginx or Apache, Gunicorn | A lightweight, flexible micro-framework that grants developers full control without imposing a rigid structure. Ideal for small applications, prototypes, or services requiring maximum customization. |
| [Pyramid](https://trypyramid.com/) | [Python](https://www.python.org/), [Pyramid](https://trypyramid.com/), various databases | A flexible framework that scales from minimal applications to large systems. It allows developers to choose components as needed and is well-suited for projects that evolve gradually over time. |

### 4. .NET Stack

Built upon C# and the .NET ecosystem, this stack is used to construct web applications, APIs, and backend services.

| Stack | Core Components | Description |
| --- | --- | --- |
| [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/) | [C#](https://learn.microsoft.com/en-us/dotnet/csharp/), [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/), SQL Server or PostgreSQL, IIS or Nginx | A high-performance, cross-platform framework from Microsoft for building web apps, REST APIs, and backend services. Runs on Windows, Linux, and macOS, making it ideal for enterprise environments within the Microsoft ecosystem. |
| [Blazor Stack](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor) | [C#](https://learn.microsoft.com/en-us/dotnet/csharp/), [Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor), [.NET](https://dotnet.microsoft.com/), SQL Server or PostgreSQL | Enables interactive web UIs using C# instead of JavaScript, via Blazor WebAssembly (client-side) or Blazor Server (server-side). Ideal for .NET teams looking to build rich frontends without relying heavily on JavaScript. |

### 5. Java Stack

A stack built on Java, commonly used for scalable backend systems and enterprise-grade applications.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Java-Spring](https://spring.io/projects/spring-boot) | [Java](https://dev.java/), [Spring Boot](https://spring.io/projects/spring-boot), various databases, Tomcat | The most widely adopted Java framework for building backends and microservices. Spring Boot simplifies configuration and provides production-ready features such as health checks, metrics, and externalized configuration. |
| [Jakarta EE](https://jakarta.ee/) | [Java](https://dev.java/), [Jakarta EE](https://jakarta.ee/), various databases, application server | An open enterprise Java standard for large-scale applications, covering web, enterprise beans, and messaging. Commonly used in banking, telecommunications, and the public sector where open standards are essential. |
| [Quarkus](https://quarkus.io/) | [Java](https://dev.java/), [Quarkus](https://quarkus.io/), various databases | A Java framework optimized for Kubernetes and serverless environments, offering fast startup times and low memory consumption. Ideal for cloud-native microservices, particularly when compiled to GraalVM native images. |

### 6. Ruby Stack

A stack centered around Ruby, known for its strong conventions and emphasis on rapid web development.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Ruby on Rails](https://rubyonrails.org/) | [Ruby](https://www.ruby-lang.org/), [Rails](https://guides.rubyonrails.org/getting_started.html), PostgreSQL or MySQL, Puma or Unicorn | A full-stack framework that follows "Convention over Configuration". It provides migrations, scaffolding, asset pipelines, and more out of the box. Ideal for startups and MVPs that require development at high velocity. |
| [Sinatra](https://sinatrarb.com/) | [Ruby](https://www.ruby-lang.org/), [Sinatra](https://sinatrarb.com/), various databases | A minimal, lightweight Ruby micro-framework. Ideal for building simple services, small APIs, or applications that don't require the full structure of Rails. |

### 7. Go Stack

A stack built with Go (Golang), designed for high-performance backends, APIs, and microservices.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Gin](https://gin-gonic.com/) | [Go](https://go.dev/), [Gin](https://gin-gonic.com/), various databases | A fast, lightweight web framework reminiscent of Express.js. Ideal for building REST APIs and microservices with high performance and quick compilation. |
| [Echo](https://echo.labstack.com/) | [Go](https://go.dev/), [Echo](https://echo.labstack.com/), various databases | A high-performance framework with robust features such as middleware, routing, and validation. Known for its efficient memory usage and suitability for high-throughput applications. |
| [Fiber](https://docs.gofiber.io/) | [Go](https://go.dev/), [Fiber](https://docs.gofiber.io/), various databases | Inspired by Express.js and built on top of Fasthttp, Fiber is extremely fast and lightweight. Ideal for microservices and applications where low latency and minimal resource usage are critical. |
| [Go Standard Library](https://go.dev/) | [Go](https://go.dev/), `net/http`, various databases | A framework-free approach using Go's built-in standard library. Offers maximum control, minimal dependencies, and is ideal for lightweight applications with no unnecessary overhead. |

### 8. Rust Stack

A stack built with Rust, prioritizing memory safety, concurrency, and system-level performance.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Actix Web](https://actix.rs/) | [Rust](https://www.rust-lang.org/), [Actix Web](https://actix.rs/), various databases | One of Rust's fastest web frameworks, built on an actor model. Ideal for applications requiring memory safety, high concurrency, and maximum performance without a garbage collector. |
| [Axum](https://github.com/tokio-rs/axum) | [Rust](https://www.rust-lang.org/), [Axum](https://github.com/tokio-rs/axum), [Tokio](https://tokio.rs/), various databases | A modular, type-safe web framework from the Tokio ecosystem. Leverages Rust's async/await and is well-suited for building efficient, maintainable asynchronous APIs. |
| [Rocket](https://rocket.rs/) | [Rust](https://www.rust-lang.org/), [Rocket](https://rocket.rs/), various databases | A developer-friendly Rust framework that emphasizes ergonomics. Offers features such as templating, form handling, and database integration with a clean, declarative syntax. |

### 9. Infrastructure and Observability

Stacks that combine operating systems, web servers, databases, or supporting tools for infrastructure management and application observability.

| Stack | Core Components | Description |
| --- | --- | --- |
| [Wazuh](https://wazuh.com/) | [Wazuh Server](https://documentation.wazuh.com/current/) (manager, indexer, dashboard), [Wazuh Agent](https://documentation.wazuh.com/current/), [Elasticsearch](https://www.elastic.co/elasticsearch) or [OpenSearch](https://opensearch.org/) (optional), [Kibana](https://www.elastic.co/kibana) or [Wazuh Dashboard](https://documentation.wazuh.com/current/) (optional) | An open-source platform for intrusion detection, security monitoring (XDR/SIEM), log analysis, file integrity monitoring, and threat response. Ideal for centralized security monitoring across servers and endpoints. |
| [Elastic Stack (ELK)](https://www.elastic.co/elastic-stack) | [Elasticsearch](https://www.elastic.co/elasticsearch), [Logstash](https://www.elastic.co/logstash), [Kibana](https://www.elastic.co/kibana) | Used to collect, search, analyze, and visualize logs and system metrics. Ideal for monitoring, troubleshooting, and Security Information and Event Management (SIEM). |
| [Prometheus + Grafana](https://prometheus.io/) | [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), various exporters | An open-source monitoring stack that collects time-series metrics from systems and applications and visualizes them through Grafana dashboards. Ideal for infrastructure monitoring and alerting. |
| [TICK Stack](https://docs.influxdata.com/influxdb/v2/get-started/) | [Telegraf](https://docs.influxdata.com/telegraf/), [InfluxDB](https://www.influxdata.com/products/influxdb/), [Chronograf](https://docs.influxdata.com/chronograf/), [Kapacitor](https://docs.influxdata.com/kapacitor/) | A stack for collecting, storing, visualizing, and processing time-series data. Commonly used for infrastructure monitoring, IoT, and tracking application metrics over time. |

> *Note:* Choosing the right ingredients makes for a delicious meal that keeps customers coming back. However, every choice involves trade-offs—just as with technology stacks. This is not an exhaustive or prescriptive list; components within a stack may be substituted to suit specific needs.

## Choosing a Platform to Run the Stack

Once a technology stack has been chosen, the next step is to determine the **platform on which the stack will run**. The options range from physical servers (_bare metal_) and _virtual machines_ (VMs) to _containers_, as well as cloud-based offerings such as PaaS and _serverless_.

In server terms, this choice affects how the application runs, how computing resources are provisioned, and how the infrastructure is managed. Reference: [Wikipedia — Computing platform](https://en.wikipedia.org/wiki/Computing_platform).

```mermaid
flowchart TD
    A["🍜 Stack is ready<br/>recipe + ingredients + tools"] --> B{"📍 Where to run it?"}
    B --> C["🏠 Bare Metal<br/>Build your own eatery"]
    B --> D["🛏️ Virtual Machine<br/>Rent a private room"]
    B --> E["🍱 Container<br/>Rent a stall in a food court"]
    B --> F["🏪 PaaS<br/>Join a ready-to-use franchise"]
    B --> G["🛒 Serverless<br/>Open a stall only when orders come in"]
    B --> H["🛵 Edge Computing<br/>Use a food cart near your customers"]
    C --> I["🧩 All stack components<br/>run in one place"]
    D --> I
    E --> I
    F --> I
    G --> I
    H --> I
```

Imagine you've gathered your recipe, ingredients, and tools to open an eatery. You must now decide where to operate: build your own premises, rent a space, share facilities with others, or open a temporary stall as needed.

In server terms, these choices are analogous:

| Environment | Eatery Analogy | Description | Examples |
| --- | --- | --- | --- |
| **Bare Metal / Dedicated Server** | Build an eatery on your own land. You have full control over everything, from walls to stoves. | The OS and applications run directly on physical hardware with no hypervisor. | [IBM Bare Metal Servers](https://www.ibm.com/think/topics/bare-metal-servers), [OVHcloud Dedicated Server](https://www.ovhcloud.com/en/bare-metal/) |
| **Virtual Machine (VM) - Desktop** | Rent a private room in a boarding house. Yours alone, and you can reset it anytime if something goes wrong. | A virtual computer with its own OS running on your personal machine. | [VirtualBox](https://www.virtualbox.org/), [VMware Workstation](https://www.vmware.com/products/workstation-pro.html), [VMware Fusion](https://www.vmware.com/products/fusion.html) |
| **Server Virtualization Platform** | The boarding house owner manages dozens of rooms from a central office. | Manages multiple VMs on a production server through a centralized interface. | [VMware vSphere / ESXi](https://www.vmware.com/products/vsphere.html), [Proxmox VE](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) |
| **Container** | Rent a stall in a food court. You share kitchen facilities, but your stall is isolated and easy to move. | Applications run in isolated packages that share the host OS kernel. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) |
| **PaaS (Platform as a Service)** | Open a ready-to-use franchise. Bring your recipe; the shop, utilities, and infrastructure are provided. | The provider manages infrastructure; you only need to upload your code. | [Heroku](https://www.heroku.com/), [Render](https://render.com/), [Railway](https://railway.app/) |
| **Serverless / FaaS** | A pop-up stall at an event. Open only when customers arrive, close when quiet, and pay per order. | Code runs on demand with no permanently managed server. | [AWS Lambda](https://aws.amazon.com/lambda/), [Azure Functions](https://learn.microsoft.com/azure/azure-functions/), [Cloudflare Workers](https://workers.cloudflare.com/) |
| **Shared Hosting** | A street-side stall shared by many vendors. Affordable, but crowded and limited in control. | Multiple users share the same server resources. | [cPanel](https://cpanel.net/), [Hostinger](https://www.hostinger.com/) |
| **Managed Hosting** | Rent a shop with a manager who handles day-to-day operations. | The provider takes care of most server management and operations. | [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) |
| **Edge Computing** | A food cart parked near customers to serve food faster. | Processing is done closer to users to reduce latency. | [Cloudflare Workers](https://workers.cloudflare.com/), [AWS Wavelength](https://aws.amazon.com/wavelength/) |

### Key Distinctions

- **VMware Workstation and Fusion** are for local desktop virtualization, ideal for learning at home.
- **VMware ESXi/vSphere and Proxmox VE** are for production server virtualization, ideal for managing many VMs at scale.
- **Bare Metal** refers to software running directly on physical hardware. A **Dedicated Server** refers to a physical server rented to a single customer. The terms are related but not synonymous.

### Relation to Single-Tier Stack

A **single-tier** architecture means all stack components ([web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), [application runtime](https://en.wikipedia.org/wiki/Runtime_system), and [database](https://en.wikipedia.org/wiki/Database)) reside in **the same place** — for example, within a single VM, a single container, or a single physical server.

However, single-tier does **not** require using a VM or container. The stack can also run on bare metal, a dedicated server, or even PaaS, as long as all components remain on the same platform.

It is important to distinguish:

- **Platform** = the environment where the stack runs (bare metal, VM, container, PaaS, serverless, etc.).
- **Tier architecture** = how application components are divided (single-tier, multi-tier, etc.).

The choice of platform affects operational costs, flexibility, scalability, security, and maintainability. There is no universally optimal choice — everything depends on the needs of the project.

## Tips to Get Started

1. **Understand the application flow**  
   Learn how an [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) travels from the browser to the [web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), how it's processed by the application, and how the [database](https://en.wikipedia.org/wiki/Database) is used if needed before returning an [HTTP response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). Run a simple app and observe status codes like `200 OK`, `404 Not Found`, and `500 Internal Server Error` to see the difference between successful and failed requests.  
   Reference: [MDN — How the Web Works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)

2. **Choose the right technology stack**  
   Pick a stack based on your application needs, team skills, documentation, security, performance, and cost. For learning, start with a simple one like [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)) or [LEMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)#LEMP) for PHP, or [MERN](https://www.mongodb.com/resources/languages/mern-stack) for JavaScript. Learn the role of each component before adding more tools.

3. **Start in a local environment**  
   Build and run your stack on your own machine using a local install, [VirtualBox](https://www.virtualbox.org/) for a virtual machine (VM), or [Docker](https://www.docker.com/) for a container. Try starting, stopping, and restarting it to understand configuration and dependencies. Note the difference: VMs run their own guest OS, while containers share the host kernel.  
   Reference: [Docker — What is a Container?](https://www.docker.com/resources/what-container/)

4. **Test your application after running it**  
   A stack that starts doesn't always work correctly. Access it through a browser, check the HTTP response, verify request handling, and test database read/write operations if used. To practice troubleshooting, stop one component in a test environment, observe errors and logs, then restart it to see if the app recovers.  
   Reference: [Docker — Run Your First Container](https://docs.docker.com/get-started/)

5. **Learn HTTP and HTTPS before implementing TLS**  
   Understand the difference between HTTP and HTTPS first. In a test environment, access your app over HTTP, then enable HTTPS with a test certificate. Observe protocol differences, certificate validation, and browser warnings for untrusted or invalid certificates.  
   Once you understand this, use HTTPS with a valid certificate for public sites. [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) encrypts communication, authenticates the server, and ensures integrity, but it won't secure your application code, authentication, or database by itself.  
   Reference: [OWASP — Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

6. **Measure performance before optimizing**  
   Track CPU, RAM, disk usage, response times, and logs under normal load. Then run controlled load tests and compare results. Look for rising resource usage or slower responses. If issues appear, change one thing at a time, measure again, and only optimize after seeing measurable impact.  
   Reference: [Prometheus — Overview](https://prometheus.io/docs/introduction/overview/)

7. **Test caching and backup recovery**  
   If your app reads the same data often, compare response times and database load before and after adding a [cache](https://en.wikipedia.org/wiki/Cache_(computing)). Check that cached data stays consistent when the source data changes.  
   For important data, create a backup of your database and app files, then restore it to a test environment. Verify the restored data is readable and usable — creating a backup doesn't guarantee you can recover from it.  
   Reference: [PostgreSQL — Backup and Restore](https://www.postgresql.org/docs/current/backup.html)

8. **Document your configuration and changes**  
   Keep track of software versions, dependencies, key configurations, and setup steps. Use [Git](https://git-scm.com/) to version-control your code and track changes. As a test, rebuild your environment from scratch using only your documentation — if you can do it without relying on memory, it's good enough.  
   Reference: [Pro Git — About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

9. **Know the limits of a single-tier stack**  
   In a single-tier setup, the [web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), [application runtime](https://en.wikipedia.org/wiki/Runtime_system), and [database](https://en.wikipedia.org/wiki/Database) all run on the same machine. A failure or resource exhaustion on that machine can bring down the entire app.  
   Test this in a safe environment by stopping one component or simulating high load. If your needs grow, evaluate optimizations, scaling up, redundancy, or splitting components across separate services based on measured needs, availability goals, and cost.  
   Reference: [Red Hat — What Is High Availability?](https://www.redhat.com/en/topics/availability/what-is-high-availability)

## Formula for Choosing a Stack and Deployment Environment

- **For learning:** personal interest + ease of use + documentation + availability of learning resources.
- **For a new project:** application requirements + user count and usage patterns + team expertise + security + performance testing + operational costs.
- **For migrating a stack or deployment:** issues with the current system + measurable benefits of migration + costs and risks + compatibility + user impact + long-term support.

**In essence:** Choose your stack and deployment environment based on application needs, user scale, team capabilities, security, cost, and testing results. To learn from real-world practice, study engineering case studies from companies that have faced similar challenges.

### Real-World Stack References

Choosing a technology stack can be overwhelming given the vast array of languages, frameworks, databases, and tools. Beyond feature comparisons, learning from companies that have built and operated systems at scale is invaluable:

- [Uber Engineering](https://www.uber.com/us/en/blog/engineering/) — Backend architecture and scalability
- [Shopify Engineering](https://shopify.engineering/) — Monoliths and database scalability
- [Cloudflare Blog](https://blog.cloudflare.com/) — Server infrastructure and networking
- [Netflix TechBlog](https://netflixtechblog.medium.com/) — Distributed systems and reliability
- [Stripe Engineering](https://stripe.com/blog/engineering) — Backend, APIs, and data consistency
- [Discord Blog](https://discord.com/category/engineering) — Real-time systems and performance optimization
- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) — Cloud architecture and deployment

**Tip:** Pay attention to the rationale behind technology choices, the problems encountered, and the trade-offs considered. Treat their experience as guidance, and adapt it to fit your own project's needs.

## Conclusion

**Server Single-Tier Stack** is an architecture where the core application components—[web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server), [application runtime](https://en.wikipedia.org/wiki/Runtime_system), and [database](https://en.wikipedia.org/wiki/Database)—all run on a single machine.

Much like a small eatery operating in one location, a browser sends an [HTTP Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) to the server, the application processes it (and queries the database if needed), and returns an [HTTP Response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to the user.

By distinguishing between *core components* (OS, web server, application runtime, and database) and *supporting components* (web client, TLS & TLS certificate, and cache), it's easier to identify what is required to run an application and what can be added to improve security, performance, or user experience.

There are many technology stacks to choose from—such as LAMP, MERN, Django, Spring Boot, and more—depending on project needs. These stacks can run on various platforms, from bare metal and VMs to containers, PaaS, and serverless.

While simple, easy to learn, configure, and test, a single-tier architecture has limited resources and carries the risk of being a *Single Point of Failure* (SPOF), since all components rely on the same machine.

**In short:** Start with a single-tier architecture to build a solid foundation of how servers work. Choose the right stack and platform for your needs, apply security best practices, test thoroughly, and document well. As your application grows and demands greater scalability and availability, consider moving to a multi-tier architecture.
