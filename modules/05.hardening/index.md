---
duration: 1h
---
## Hardening
 
Hardening a Linux system involves strengthening its security by reducing vulnerabilities and limiting potential entry points for cyberattacks. Here are some essential measures for hardening a Linux system:

**Limit application privileges**  
    Use modules like AppArmor (for Debian) or SELinux (for Red Hat) to control application rights and permissions.

- **AppArmor**

 - **Ease of Use**  
      AppArmor is often considered easier to configure and use compared to SELinux. It uses profiles to define application permissions, simplifying the management of security rules.

  - **Path-Based Protection**  
      AppArmor enforces security policies based on file and directory paths. This allows specifying which resources an application can access based on their location.

  - **Efficiency**  
      Being directly integrated into the Linux kernel, AppArmor is generally more efficient in terms of performance.

- **SELinux**

  - **Power and Flexibility**  
      SELinux is more powerful and flexible than AppArmor. It uses label-based policies to control resource access, offering more granular control.

  - **Mandatory Access Control (MAC)**  
      SELinux enforces mandatory access control, meaning security policies are strictly applied and cannot be bypassed by users.

  - **Enhanced Security**  
      SELinux is often used in environments requiring high security levels, such as servers and critical systems. It offers advanced features like Multi-Level Security (MLS) and Multi-Category Security (MCS).

- **Comparison**

  - **Configuration**  
      AppArmor is simpler to configure, making it suitable for less experienced users. SELinux, on the other hand, requires a deeper understanding of security concepts.

  - **Performance**  
      AppArmor may be more performant due to its direct kernel integration, while SELinux, though more complex, provides more robust security.

  - **Usage**  
      AppArmor is commonly used on desktop systems and distributions like Ubuntu, whereas SELinux is preferred for servers and distributions like Red Hat Enterprise Linux.

In summary, the choice between AppArmor and SELinux depends on specific security needs and ease of use. If you need a simple and effective solution, AppArmor might be the right choice. For environments requiring enhanced security and granular control, SELinux is more appropriate.

**Enable strong authentication**  
  Use robust passwords and enable two-factor authentication (2FA) for enhanced security.
  
  - **Minimum Length**  
    Passwords must be a certain minimum length, often between 8 to 12 characters, to offer better protection.

  - **Complexity**  
    Passwords should include a mix of different character types, such as

  - **Regular Expiration**  
    Users are often required to change their passwords at regular intervals, such as every 90 days, to limit the lifespan of a potentially compromised password.

  - **Prohibition of Reuse**  
   Users are prohibited from reusing old passwords or making only minor changes to old passwords when creating a new one.

  - **Avoiding Common or Easy-to-Guess Passwords**  
    The policy might forbid the use of overly simple or common passwords like "password," "123456," or "qwerty."

  - **Password Strength Checkers**  
    Some systems may include tools that assess the strength of a password when it is created and reject passwords that are deemed too weak.

  - **Two-Factor Authentication (2FA)**  
    Although not strictly part of the password policy, adding two-factor authentication enhances security by requiring an additional proof of identity beyond just the password.

  - **Create SSH key pairs**  
    SSH keys offer superior security compared to passwords by making brute-force attacks more difficult.

**Keep the system updated**  
  Regularly install updates and security patches to address vulnerabilities.
 - **Critical Updates**  
    Prioritize the deployment of critical security patches that address severe vulnerabilities. These updates should be applied as soon as they are available.

 - **Risk Classification**  
    Categorize updates based on their level of criticality (high, medium, low) depending on the potential impact on security.

 - **Automatic Updates**  
    Enable automatic updates for critical security patches to minimize the vulnerability window.
 
 - **Management Tools**  
   Use tools like `WSUS` for Windows or `Landscape` for Ubuntu to manage and automate updates across the IT environment.

 - **Test Environment**  
    Test patches in an isolated environment before deploying them to production systems to ensure they do not introduce new vulnerabilities or affect operations.

 - **Impact Analysis**  
    Assess the potential impact of updates on security and compliance before deployment.


**Configure firewalls**  

  Use firewalls like `iptables` or `firewalld` to control incoming and outgoing network traffic.

 - **Restrict Access to the Firewall**  

   - **Admin Access**  
    Limit access to the firewall management interface to only trusted administrators. Use secure management protocols such as SSH (instead of Telnet) and HTTPS (instead of HTTP).

   - **Multi-Factor Authentication (MFA)**  
    Require MFA for accessing the firewall management console to add an additional layer of security.

   - **IP Whitelisting**  
    Restrict access to the firewall management interface to specific IP addresses or ranges.

 - **Harden Firewall Rules**  

   - **Principle of Least Privilege**  
    Apply the principle of least privilege by creating rules that only allow the minimum necessary traffic. Deny all other traffic by default (`deny all` rule).

   - **Explicit Allow Rules**  
    Define specific allow rules for necessary traffic, specifying source and destination IPs, ports, and protocols.

   - **Regular Review**  
    Regularly review and audit firewall rules to remove obsolete or overly permissive rules that could introduce vulnerabilities.

 - **Log and Monitor Traffic**  
  
   - **Enable Logging**  
    Enable logging of all allowed and denied traffic. Logs should be detailed enough to provide insights into traffic patterns and potential threats.
  
   - **Log Analysis**  
    Implement automated log analysis tools to detect suspicious activities, such as unexpected traffic patterns or repeated access attempts.

   - **Centralized Logging**  
    Use a centralized logging system (e.g., SIEM) to aggregate and analyze logs from all firewalls in the network for better monitoring and incident response.

 - **Conduct Regular Security Audits**   
  
   - **External Audits**  
     Periodically conduct external security audits of the firewall configuration and rules to identify potential weaknesses or misconfigurations.
  
   - **Penetration Testing**  
    Engage in penetration testing to assess the firewall’s resilience against attacks and adjust configurations as needed.

**Disable unnecessary services**  
  Reduce the attack surface by disabling unnecessary services and daemons.

- **Reduced Attack Surface**  
  Each running service can potentially be exploited if it has vulnerabilities. By disabling services that are not needed, you reduce the number of potential entry points for an attacker.

- **Lower Resource Usage** 
  Unnecessary services consume system resources (CPU, memory, and network bandwidth), which can be better utilized by essential applications.

- **Decreased Complexity**  
  Fewer running services make system management simpler and can reduce the risk of misconfigurations and conflicts.

**Monitor system logs**  
  Use tools like logwatch or syslog to monitor logs and detect suspicious activities.

**Regularly backup data**  
Perform regular backups and test them to ensure they can be restored if needed.

These measures will help you strengthen the security of your Linux systems and protect them against cyberattacks.

