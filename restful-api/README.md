# RESTful API

How to communicate and transfer data efficiently between systems?

RESTful APIs, a cornerstone in the realm of web services.

The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

HTTP is a protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. A complete document is typically constructed from resources such as text content, layout instructions, images, videos, scripts, and more.

HTTP means Hyper Text Transfer Protocol
- Hyper in mathematical sense means extension
- Text is an object that can be "read" (a set of signs that is available to be reconstructed by a reader)
- Transfer is move things to one place to another
- Protocol is how things must be layed out or done to meet certain criteria

## 0. Basics of HTTP/HTTPS

The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

Differentiating HTTP and HTTPS:

| Feature                 | **HTTP**                                                      | **HTTPS**                                                   |
| ----------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| **Encryption**          | ❌ No encryption – data is sent in **plain text**              | ✅ Uses **SSL/TLS** to encrypt data during transfer          |
| **Data Protection**     | ❌ Vulnerable to **eavesdropping** (man-in-the-middle attacks) | ✅ Protects against snooping and tampering                   |
| **Authentication**      | ❌ No built-in way to verify the server’s identity             | ✅ Uses **SSL certificates** to verify the server is trusted |
| **Data Integrity**      | ❌ No guarantees – data can be altered in transit              | ✅ Ensures **data hasn’t been modified** during transmission |
| **URL Prefix**          | `http://`                                                     | `https://`                                                  |
| **Port Used**           | Port **80**                                                   | Port **443**                                                |
| **SEO & Browser Trust** | 🚫 Browsers mark as “Not Secure”                              | ✅ Shows 🔒 padlock icon; preferred by search engines        |


| HTTP Method | CRUD Operation |
| ----------- | -------------- |
| GET         | Read           |
| POST        | Create         |
| PUT         | Update         |
| DELETE      | Delete         |
