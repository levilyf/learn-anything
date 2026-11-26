# Example: cybersecurity concept map

**Purpose:** show how foundational networking concepts relate to a basic web request.

```mermaid
flowchart TD
    A[Domain name] --> B[DNS resolution]
    B --> C[IP address]
    C --> D[Network connection]
    D --> E[Web server]
    F[HTTP request] --> E
    E --> G[HTTP response]
    H[Transport protocol] --> D
```

**What to notice:** DNS resolution helps the client discover an IP address. The network connection provides a path to the server. HTTP describes the request and response exchanged with the web server. These are related steps, not interchangeable terms.

**Text fallback:** A browser resolves a domain name through DNS, uses the resulting IP address to reach a server, then exchanges an HTTP request and response.
