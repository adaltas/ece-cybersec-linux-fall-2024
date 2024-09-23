---
duration: 1h
---

# Linux File System Security

## File Permissions

### Permissions

Linux uses a permission model to control access to files and directories.
Each file and directory has three types of permissions:

- **Read (r):**  
  Allows viewing the contents of the file.
- **Write (w):**  
  Allows modifying the contents of the file.
- **Execute (x):**  
  Allows running the file if it's a script or program.

Permissions are assigned to three categories of users:

- **User:**  
  The user who owns the file.
- **Group:**  
  A set of users who share the same permissions.
- **Other:**  
  All other users.

modif absolu (ex 755), et relative (ugo+w)

### Special Permissions

- **Setuid:**  
  Allows a user to run an executable with the permissions of the executable's owner.
- **Setgid:**  
  Allows a user to run an executable with the permissions of the executable's group.
- **Sticky Bit:**  
  Applied to directories, it ensures that only the file's owner can delete or rename the file within that directory.

## File Ownership

Each file and directory is owned by a user and a group.
Ownership can be changed using the `chown` command.

## Access Control Lists (ACLs):**

ACLs provide a more flexible permission mechanism. They allow setting permissions for specific users or groups beyond the traditional user/group/others model. You can manage ACLs using the `setfacl` and `getfacl` commands.



## File Encryption

Encrypting files adds an extra layer of security. Tools like `gpg` can be used to encrypt files, ensuring that only authorized users can access the contents.

## Secure Deletion

When you delete a file, it's not immediately removed from the disk. Tools like `shred` can be used to securely delete files by overwriting them multiple times.
These mechanisms collectively help in maintaining the security and integrity of files on a Linux system.

## backup

Is the operation that
consists of duplicating and securing the data
data contained in a computer system
Note: not to be confused with archiving
(different purpose, different retention period)

Commons license.
Compression tools
- compress(1)
- gzip(1)
- bzip2(1)
- xz(1)
- 7z(1)

Commons license.
rsync(1) - Synchronize
directories
- Allows :
- copy directories within or between machines
- Synchronize directories between machines
- It's extremely powerful because it works by delta (sending only
only different blocks between source and destination

