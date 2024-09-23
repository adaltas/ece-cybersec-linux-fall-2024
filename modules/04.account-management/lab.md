---
duration: 1h
---

# Lab: Account management

Aser management on linux machines and password policy management

## Objectives

- Learn how to create new user account
- Understand how to modify existing user accounts
- Learn how to delete user accounts
- Practice adding and removing users from groups
- Understand file and directory permissions
- Learn how to manage user passwords
- Practice locking and unlocking user accounts

## Tasks

1. Part 1. Creating User Accounts (easy level)
2. Part 2. Modifying User Accounts (easy level)
3. Part 3. Deleting User Accounts (easy level)
4. Part 4. Managing User Groups (easy level)
5. Part 5. Setting Permissions (easy level)
6. Part 6. Password Management (easy level)
7. Part 7. Account Locking and Unlocking (easy level)

## Part 1. Creating User Accounts (easy level)

 Use the `useradd` command to create a new user account. Set a password for the user using the `passwd` command.
  ```bash
  sudo useradd -m newuser
  sudo passwd newuser
  ```

## Part 2. Modifying User Accounts (easy level)
Change the user's home directory and shell using the `usermod` command.
  ```bash
  sudo usermod -d /new/home/directory -s /bin/bash newuser
  ```

## Part 3. Deleting User Accounts (easy level)
Remove a user account and their home directory using the `userdel` command.
  ```bash
  sudo userdel -r newuser
  ```

## Part 4. Managing User Groups (easy level)
Add a user to a group and then remove them using the `usermod` and `gpasswd` commands.
  ```bash
  sudo usermod -aG groupname newuser
  sudo gpasswd -d newuser groupname
  ```

## Part 5. Setting Permissions (easy level)
Change the permissions of a file using the `chmod` command and change the owner using the `chown` command.
  ```bash
  sudo chmod 755 /path/to/file
  sudo chown newuser:newgroup /path/to/file
  ```

## Part 6. Password Management (easy level)
Expire a user's password and force them to change it at the next login using the `passwd` command.
  ```bash
  sudo passwd -e newuser
  ```

## Part 7. Account Locking and Unlocking (easy level)
Lock a user account and then unlock it using the `passwd` command.
  ```bash
  sudo passwd -l newuser
  sudo passwd -u newuser
  ```

## Part 8. Bash Fork Bomb Lab (easy level)

### **The Fork Bomb**

A fork bomb is a denial-of-service (DoS) attack that exploits the "fork" mechanism used by UNIX/Linux systems to create new child processes from a parent process. The idea behind a fork bomb is to create processes that repeatedly spawn new processes in a loop, rapidly exhausting system resources.

**Classic Bash fork bomb example:**
```bash
:(){ :|:& };:
```

This script uses recursion to create a large number of processes quickly. Each process creates two new processes (one via `:` and the other via `|`), and this continues until the system's resources are fully depleted.

### **Practical Experiment: Creating a Fork Bomb in a Controlled Environment**

#### **Prerequisites**:
- Use virtualization (e.g., VirtualBox, Docker) to isolate your experiment from your main machine.
- Install a lightweight Linux distribution like Ubuntu, Debian, or others.

#### **Steps**:

- **Prepare the System**:
   - Start a virtual machine (VM) or container running Linux.
   - Open a terminal as a standard user (not root).

- **Launching the Fork Bomb**:

   **Warning!** Never run this type of command on a production system or your personal machine without precautions.

   - Execute the following command in the terminal to trigger the fork bomb:
     ```bash
     :(){ :|:& };:
     ```

- **Observe the Effects**:
   - You should quickly notice your system becoming unresponsive due to process saturation.
   - Using tools like `htop` or `top`, you can observe the exponential increase in the number of running processes.

---

### **Preventing Fork Bombs: Mitigation Techniques**

#### **Limit the Number of User Processes**:
You can set limits to prevent users from creating too many processes, thereby reducing the risk of a fork bomb.

- **Set User Limits with `ulimit`**:
   - The `ulimit` command allows you to define limits on system resources for a user.
   - To limit the number of processes a user can create, run the following command:
     ```bash
     ulimit -u 100
     ```
     This sets the maximum number of processes for a user to 100.

- **Set Permanent Limits in `/etc/security/limits.conf`**:
   - You can define persistent limits by editing this file:
     ```bash
     sudo nano /etc/security/limits.conf
     ```
     Add lines like this:
     ```bash
     *       hard    nproc   100
     ```
     This sets a limit of 100 processes for all users.

3. **Restart the System**:
   - Once a fork bomb has been triggered, the only way to restore functionality is usually to restart the machine (forcing it if necessary).


### OpenLDAP

#### Objective:
- Install and configure an OpenLDAP server on Ubuntu.
- Add users and groups to the LDAP directory.
- Test the configuration using command-line tools.

#### 1. Update the Ubuntu server

Make sure your Ubuntu server is up to date before you begin.

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install OpenLDAP and related tools

Install the OpenLDAP server and necessary administration tools.

```bash
sudo apt install slapd ldap-utils -y
```

During the installation, a configuration assistant will appear to set the LDAP administrator password (for `cn=admin,dc=example,dc=com`). Make sure to choose it carefully and note it down for later use.

#### 3. Reconfigure the LDAP server

If you need to reconfigure the server to change parameters (such as the domain name or admin password), run the following command:

```bash
sudo dpkg-reconfigure slapd
```

Here are the important options to configure:

- **Omit OpenLDAP server configuration?**: No.
- **DNS domain name**: Use a domain like `example.com`. This will generate the base DN (`dc=example,dc=com`).
- **Organization name**: Choose an organization name (e.g., `Example Inc.`).
- **Administrator password**: Enter the LDAP admin password.
- **Database backend**: Leave the default (**MDB**).
- **Remove database when slapd is purged?**: No.
- **Move old database?**: Yes.

#### 4. Check the status of LDAP

Ensure that the **slapd** service is running:

```bash
sudo systemctl status slapd
sudo systemctl start slapd
```

The service should be active and running.

#### 5. Add an LDAP schema

OpenLDAP uses schemas to structure objects in the directory. The **cosine** and **inetorgperson** schemas are commonly used for users and groups.

1. Load the necessary schemas with the following commands:

```bash
sudo ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/cosine.ldif
sudo ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/inetorgperson.ldif
```

#### 6. Create a base structure for the LDAP directory

Create a **base.ldif** file that contains the basic configuration for your directory (domains, organizational units, etc.).

Create the **base.ldif** file:

```bash
sudo nano base.ldif
```

Add the following content (adjust `dc=example,dc=com` to match your domain):

```ldif
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups
```

Next, add this structure to your LDAP directory:

```bash
sudo ldapadd -x -D "cn=admin,dc=example,dc=com" -W -f base.ldif
```

Enter the LDAP admin password when prompted.

#### 7. Add users to LDAP

1. Create a **users.ldif** file to add a user to the LDAP directory.

```bash
sudo nano users.ldif
```

Add this user to the **users.ldif** file:

```ldif
dn: uid=jdoe,ou=users,dc=example,dc=com
objectClass: inetOrgPerson
uid: jdoe
sn: Doe
givenName: John
cn: John Doe
displayName: John Doe
userPassword: password123
mail: jdoe@example.com
```

2. Add this user to LDAP with the following command:

```bash
sudo ldapadd -x -D "cn=admin,dc=example,dc=com" -W -f users.ldif
```

#### 8. Add groups to LDAP

1. Create a **groups.ldif** file to add a group to LDAP.

```bash
sudo nano groups.ldif
```

Add this group to the **groups.ldif** file:

```ldif
dn: cn=developers,ou=groups,dc=example,dc=com
objectClass: posixGroup
cn: developers
gidNumber: 5000
memberUid: jdoe
```

2. Add the group to LDAP with the following command:

```bash
sudo ldapadd -x -D "cn=admin,dc=example,dc=com" -W -f groups.ldif
```

#### 9. Query the LDAP directory

You can use the **ldapsearch** command to query your LDAP directory and view users, groups, and other objects.

Example search for user `John Doe`:

```bash
ldapsearch -x -LLL -b "dc=example,dc=com" "(uid=jdoe)"
```

This will display information about the `jdoe` user.
