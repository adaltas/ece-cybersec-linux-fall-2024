---
duration: 1h
---
# Lab: Files systems management

files systems permission management

## Objectives

- Permissions files management
- owners and groups management
- ACLs
- File Encryption 
- Archive creation for backup

## Tasks

1. Part 1. Checking Permissions (easy level)
2. Part 2. Change the owner and group  (easy level)
3. Part 3. Using ACLs (easy level)
4. Part 4. Special Permissions (easy level)
5. Part 5. File Encryption (easy level)
6. Part 6. Archive creation

## Prerequisites

an available vm ubunut

## Part 1. Checking Permissions (easy level)
1. **List file permissions:**
Use the `ls -l` command to display the permissions of a file named `example.txt`.
```bash
ls -l example.txt
```

2. **Modify permissions:**
Change the permissions of `example.txt` so that the owner has all rights, the group has read and execute rights, and others have no rights.
```bash
chmod 750 example.txt
```

## Part 2. Change the owner and group (easy level)
1. **Change the owner and group of a file:**
Use the `chown` command to change the owner of `example.txt` to `user1` and the group to `group1`.
```bash
sudo chown user1:group1 example.txt
 ```

## Part 3. Using ACLs (easy level)
1. **Add an ACL for a specific user:**
Add an ACL to allow `user2` to read and write to `example.txt`.
```bash
setfacl -m u:user2:rw example.txt
```

2. **Check ACLs:**
Use the `getfacl` command to check the ACLs of `example.txt`.
```bash
getfacl example.txt
```

## Part 4. Special Permissions (easy level)
1. **Apply the setuid bit:**
Apply the setuid bit to an executable file `script.sh` so it runs with the owner's permissions.
```bash
chmod u+s script.sh
```

2. **Apply the setgid bit:**
Apply the setgid bit to a directory `shared_dir` so that files created in this directory belong to the directory's group.
 ```bash
 chmod g+s shared_dir
 ```

3. **Apply the sticky bit:**
Apply the sticky bit to a directory `public_dir` so that only the owners of the files can delete them.
```bash
chmod +t public_dir
 ```

## Part 5. File Encryption (easy level)
1. **Encrypt a file:**
 Use `gpg` to encrypt a file `secret.txt`.
 ```bash
gpg -c secret.txt
 ```

2. **Decrypt a file:**
 Use `gpg` to decrypt the file `secret.txt.gpg`.
```bash
gpg secret.txt.gpg
```