---
duration: 40min
---

# Security is Everywhere

## Introduction

Cybersecurity refers to the set of strategies, methods, solutions and tools used to protect computer systems, networks and digital data from unauthorized access, data breaches, cyberattacks and other malicious activities.
It aims to ensure the **confidentiality**, **integrity** and **availability** of information and digital resources. This includes technical measures (such as firewalls and antivirus software), organizational measures (such as security policies) and physical measures (such as locks and surveillance cameras)

### why cybersecurity is an issue at the heart of the information system ?

Cybersecurity guarantees several essential aspects to protect information systems and data. Here are the main elements it ensures.

- **Confidentiality**  
  Protecting sensitive information from unauthorized access.
- **Integrity**  
  Preservation of data accuracy and reliability, preventing unauthorized alteration.
- **Availability**  
  Ensuring that systems and data are accessible to authorized users when they need them.
- **Traceability**  
  Ability to trace actions and events to detect and analyze security incidents1.

### In which areas does cybersecurity intervene ?

Cybersecurity intervenes in various areas to protect systems, networks, and data from cyber threats. Here are the key areas:

- **Network Security**  
  Protects data during transmission across networks.
- **Information Security**  
  Protects data from unauthorized access and disclosure.
- **Application Security**  
  Secures software applications throughout their lifecycle.
- **Endpoint Security**  
  Protects individual devices from threats.
- **Cloud Security**  
  Secures data and services hosted in the cloud.
- **Critical Infrastructure Security**  
  Protects systems essential for societal functioning.
- **Identity and Access Management (IAM)**  
  Controls access to resources by authorized individuals.
- **Incident Response**  
  Prepares for and responds to security incidents.
- **Risk Management**  
  Identifies and manages risks to minimize the impact of threats.
- **Security Awareness and Training**  
  Educates users on cybersecurity best practices.


## Holistic

Cybersecurity is a crucial field within computer science that focuses on protecting computer systems, networks, and data from digital attacks.

- **Authentication**  
  Domain specific, depends on the architecture (FS, RDBMS, NoSQL, ...) and the usages.
- **Network Security**    
  Protecting computer networks from intrusions and attacks.
- **Application Security**  
  Securing software and applications against vulnerabilities.
- **Data Security**   
  Protecting sensitive data from unauthorized access and leaks.
- **Operating System Security**  
  Hardening operating systems to prevent attacks.
- **Identity and Access Management**  
  Controlling access to computing resources to ensure only authorized individuals can access them.
- **Incident Response**  
  Managing and responding to cyberattacks to minimize damage.
- **Audit and Compliance**  
  Ensuring systems comply with security standards and regulations.

### Applied to Web Development

- **HTTP encryption**  
  HTTPS by default with the launch of Let's Encrypt in 2014.
- **SQL injection**  
- **User authentication and permission**  
  Custom permission rule engine for applications, LDAP in enterprise
- **OAuth2**  
  manages who can access a resource and how to obtain access. 
- **JWT**  
  is a method for representing and verifying authentication/authorization information in exchanges

### Applied to back office systems

- **Identity Management**  
  Identity and Access Management (IAM) refers to the set of processes that manage a user’s identity on the Big Data
- **Password Management**  
  Use complex and unique passwords for each account. Enable two-factor authentication whenever possible.
- **Regular Updates**  
  Ensure all software and operating systems are up to date to benefit from the latest security patches.
- **Regular Backups**  
  Frequently back up your data to prevent loss in case of an attack or system failure.
- **Data Encryption**  
  Encrypt sensitive data both in transit and at rest to prevent unauthorized access.
- **Access Control**  
  Limit access to sensitive data to authorized personnel only and monitor access for any suspicious activity.
- **Awareness and Training**  
  Regularly train employees on best security practices and cybersecurity risks.
- **Network Security**  
  Use firewalls, antivirus software, and virtual private networks (VPNs) to protect internal networks.
- **Monitoring and Detection**  
  Implement intrusion detection systems and continuously monitor activities to quickly identify threats.

### Safety vs Security

- **Safety**  
 Protection against defects, errors, accidents, dangers,..,

- **Security**  
 Prevention of malicious acts

## Penetration Testing (Pentesting)

**Penetration Testing (Pentesting)** simulates cyberattacks to identify security vulnerabilities in systems, 
networks, or applications before hackers can exploit them. The goal is to detect and fix weaknesses, strengthening the overall security posture.

### Types of Pentests

- **External Pentest**  
  Simulates attacks from outside the network (e.g., web servers).
- **Internal Pentest**  
  Simulates attacks within the network (e.g., insider threats).
- **Web Application Pentest**  
  Identifies vulnerabilities in web applications (e.g., SQL injection).
- **Network Pentest**  
  Evaluates the security of network infrastructure.
- **Social Engineering**  
  Simulates attacks exploiting human errors (e.g., phishing).

### Phases of a Pentest

- **Planning**  
  Define the scope and objectives of the test.
- **Reconnaissance**  
  Gather information on the target (network, systems).
- **Vulnerability Scanning**  
  Identify potential vulnerabilities using tools like Nmap or Nessus.
- **Exploitation**  
  Exploit identified vulnerabilities to gain access.
- **Reporting**  
  Document vulnerabilities and provide remediation recommendations.

### Pentesting Types

- **Black Box**  
  No prior knowledge of the system.
- **White Box**  
  Full access to architecture and code.
- **Gray Box**  
  Partial knowledge of the system.

### Common Pentesting Tools

- **Nmap**
  Port scanning and network discovery.
- **Metasploit**  
  Exploitation of known vulnerabilities.
- **Burp Suite**  
  Web application security testing.
- **Wireshark**
  Network traffic analysis.

### Benefits of Pentesting

- **Improves Security**  
  by identifying and fixing vulnerabilities.
- **Ensures Compliance**  
  with security standards (e.g., ISO, PCI-DSS).
- **Strengthens Defenses**  
  against real-world cyberattacks.
