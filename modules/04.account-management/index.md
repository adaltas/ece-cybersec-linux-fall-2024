---
duration: 1h
---

## Account management

Here's an overview of Linux security at the user and group levels.

### **User Accounts**

- **UID (User ID)**  
 Each user has a unique identifier called a UID. The root account has UID 0, granting it full administrative privileges.
- **Password Management**  
  Passwords are securely stored in the `/etc/shadow` file, which is accessible only by the root user. It's crucial to use strong passwords and change them regularly.

### 2. **Groups**

- **GID (Group ID)**  
  Groups are identified by a GID. A user can belong to multiple groups, allowing for more flexible permission management.
- **Default Groups**  
  When a user is created, a group with the same name as the user is also created. This helps manage file and directory permissions individually.

### **File Permissions**

- **Read, Write, Execute**  
  File permissions in Linux are defined for the owner, the group, and others. They are represented by letters (r, w, x) and numbers (0-7).
- **Commands `chmod`, `chown`, `chgrp`**:   
  These commands allow you to change the permissions and ownership of files and directories.

### **Privilege Management Tools**

- **`su` (substitute user)**  
  This command allows you to switch users within a session. Without arguments, it switches to the root user.
- **`sudo` (substitute user do)**   
  Allows specific users to execute commands with elevated privileges without logging in as root. Permissions are defined in the `/etc/sudoers` file.

### **Best Practices**

- **Use Groups for Permissions**  
  Create groups for each project or service to simplify rights management.
- **Limit Privileges**: Do not grant administrative rights to all users. Use `sudo` to grant specific permissions temporarily.

These elements help secure a Linux system by controlling access to resources and limiting user privileges.

## LDAP Technology

**LDAP (Lightweight Directory Access Protocol)**  
  is a protocol used to access and manage distributed directory services over an IP network. It allows for the storage and organization of information in a hierarchical structure, making it easier to manage users, groups, and resources.

### Key Features:

- **Hierarchical Structure** 
   Data is organized in a tree-like structure, which allows for efficient information management.
- **Authentication and Authorization**  
  LDAP is commonly used to authenticate users and control their access to network resources.
- **Interoperability**  
  Compatible with various systems and applications, LDAP is often used alongside other protocols like Kerberos and SAML.

## Existing LDAP Solutions

- **OpenLDAP**:
- **Description**
   An open-source implementation of LDAP, widely used for its flexibility and advanced features.
- **Usage**  
  Ideal for environments that require extensive customization and integration.

- **Microsoft Active Directory (AD)**
   - **Description**
     A proprietary LDAP solution from Microsoft, integrated with 
   Windows systems for managing users and resources.
   - **Usage**  
     Preferred in Windows environments for its ease of integration and additional features.

- **Apache Directory**
   - **Description**  
     An open-source LDAP server developed by the Apache Foundation, known for its modularity and extensibility.
   - **Usage**  
     Suitable for projects needing a lightweight and extensible LDAP solution.

- **389 Directory Server**:
   - **Description** 
     An open-source LDAP server developed by Red Hat, designed to be highly performant and secure.
   - **Usage**  
    Used in enterprise environments requiring a robust and scalable solution.

- **OpenDJ**:
   - **Description**  
     An open-source LDAP solution derived from Sun Microsystems, offering advanced features and high reliability.
   - **Usage**  
    Suitable for large organizations needing a reliable and high-performance directory management solution.

These solutions provide a variety of options to meet specific identity and access management needs in different environments.