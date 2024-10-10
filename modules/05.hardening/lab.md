---
duration: 1h
---

# Lab: Hardening vm linux

securing a linux machine

## Objectives

- Ensure your system is up-to-date with the latest security patches
- Set up a firewall to control incoming and outgoing traffic
- Reduce the attack surface by disabling services you don't need
- Enhance SSH security by using key-based authentication
- Protect against brute-force attacks
- Monitor your system for suspicious activities
- Protect sensitive data by encrypting it
- Ensure data integrity and availability
- 

## Tasks

1. Part 1. update and Upgrade System (easy level)
2. Part 2. Configure a Firewall (easy level)
3. Part 3. Disable Unnecessary Services (easy level)
4. Part 4. SSH Key Authentication (easy level)
5. Part 5. Set Up Fail2Ban (easy level)
6. Part 6. Implement Intrusion Detection System (IDS) (easy level)
7. Part 7. Encrypt Data at Rest (easy level)
8. Part 8. Regular Backups (easy level)

## Prerequisites

Have a hypervisor installed and operational 

## Part 1. update and Upgrade System (easy level)
Run the following commands to update and upgrade your system.
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

## Part 2. Configure a Firewall (easy level)
Use `ufw` (Uncomplicated Firewall) to allow only necessary ports.
  ```bash
  sudo ufw allow ssh
  sudo ufw allow http
  sudo ufw enable
  ```

## Part 3. Disable Unnecessary Services (easy level)
List all running services and disable any unnecessary ones.
  ```bash
  sudo systemctl list-unit-files --type=service
  sudo systemctl disable service_name
  ```
Listing All Services

```bash
sudo systemctl list-unit-files --type=service
```
- **`systemctl`**: This is the primary tool used to interact with the "systemd" service manager, which manages services and units on modern Linux systems.
- **`list-unit-files`**: This command shows you all the unit files (services) available on your system, whether they are active or not.
- **`--type=service`**: This option filters the output to only show units of type **service**, so you will see the list of system services (e.g., `apache2.service`, `ssh.service`, etc.).

The output will display a list of services with two main columns:
- **UNIT FILE**: The name of the service (e.g., `apache2.service`).
- **STATE**: The state of the service. This can be:
  - `enabled`: The service is set to start automatically at boot.
  - `disabled`: The service is disabled and will not start automatically.
  - `static`: The service can be activated by other services but does not start on its own.
  - `masked`: The service is disabled and blocked from being started.

Disabling an Unnecessary Service

```bash
sudo systemctl disable service_name
```
- **`disable`**: This command disables the specified service, preventing it from starting automatically at the next system boot.
- **`service_name`**: This is the name of the service you want to disable. For example, to disable Apache, you would use:

```bash
sudo systemctl disable apache2.service
```

#### Note:
Disabling a service does not stop it immediately if it is already running. If you also want to stop the service, use the following command:

```bash
sudo systemctl stop service_name
```

Example to stop Apache:

```bash
sudo systemctl stop apache2.service
```
Identifying Unnecessary Services

To determine which services you can disable, here are some tips:
- **Check for services you are not using**: For instance, if you are not running a web server on your personal computer, you can disable `apache2`, `nginx`, or any other server-related service.
- **Look for services specific to software you do not use**: For example, if you are not using Docker, you can disable `docker.service`.
- **Do not disable critical services** such as `networking`, `ssh`, or those related to log management or power management (`acpid`, `systemd-logind`, etc.).

### 4. Checking Running Services

If you want to see only the services that are **currently running**, use this command:

```bash
sudo systemctl --type=service --state=running
```

This will give you a more precise view of the active services, and you can then decide which ones to disable if you are not using them.



## Part 4. SSH Key Authentication (easy level)
Here's a detailed explanation of the commands you've provided for generating SSH keys and disabling password authentication on a server:

Generate SSH Keys

```bash
ssh-keygen -t rsa -b 4096
```
- **`ssh-keygen`**: This command is used to generate new SSH key pairs.
- **`-t rsa`**: This option specifies the type of key to create. In this case, you are creating an RSA key.
- **`-b 4096`**: This option sets the number of bits in the key. A key size of 4096 bits is recommended for strong security.

Steps After Running the Command:
- **Choose a Location**: After running the command, you will be prompted to specify a location to save the key. By default, it will be saved as `~/.ssh/id_rsa` (private key) and `~/.ssh/id_rsa.pub` (public key). You can press Enter to accept the default or provide a different path.
  
- **Set a Passphrase (Optional)**: You will be prompted to enter a passphrase for additional security. You can choose to leave it empty, but adding a passphrase adds an extra layer of security.

Copy the Public Key to the Server

```bash
ssh-copy-id user@server
```
- **`ssh-copy-id`**: This command installs your public key on the remote server, allowing you to authenticate using your private key instead of a password.
- **`user@server`**: Replace `user` with your username on the remote server and `server` with the server's hostname or IP address.

Steps After Running the Command:
- You will be prompted to enter the password for the remote user. Once you enter the correct password, the public key will be copied to the `~/.ssh/authorized_keys` file on the remote server, enabling passwordless authentication.

Edit the SSH Configuration

```bash
sudo nano /etc/ssh/sshd_config
```
- **`sudo`**: This command is used to run commands with elevated privileges.
- **`nano`**: This is a text editor in the terminal. You can use any text editor of your choice (like `vim` or `vi`).
- **`/etc/ssh/sshd_config`**: This is the configuration file for the SSH daemon (sshd). You will edit this file to disable password authentication.

Steps to Edit the File:
- Find the line that says `#PasswordAuthentication yes` (the `#` indicates that the line is commented out).- Change it to:

   ```bash
   PasswordAuthentication no
   ```

Restart the SSH Daemon

```bash
sudo systemctl restart sshd
```
- **`systemctl`**: This command is used to control the systemd system and service manager.
- **`restart`**: This option restarts the specified service.
- **`sshd`**: This is the name of the SSH daemon service.

#### Result:
After restarting the SSH service, the changes you made to the configuration file will take effect. Password authentication is now disabled, and only SSH key-based authentication will be allowed.

### Important Considerations
- **Backup Access**: Before disabling password authentication, ensure you have your SSH keys set up correctly and test the connection to the server. You can open a new terminal and attempt to SSH into the server using your key. 
  ```bash
  ssh user@server
  ```
  If you cannot log in, you might lock yourself out.
  
- **Firewall and Other Security Measures**: Make sure you have other security measures in place, such as a firewall and potentially using `fail2ban` to protect against brute-force attacks.

- **Public Key Management**: If you ever need to add another user or device that requires access to the server, you'll need to add their public key to the `authorized_keys` file on the server.

By following these steps, you've successfully generated SSH keys and disabled password authentication, enhancing the security of your SSH access to the server.

## Part 5. Set Up Fail2Ban (easy level)
Install and configure Fail2Ban to ban IPs after multiple failed login attempts.
  ```bash
  sudo apt install fail2ban
  sudo systemctl enable fail2ban
  sudo systemctl start fail2ban
  ```

## Part 6. Implement Intrusion Detection System (IDS) (easy level)
Install and configure an IDS like `AIDE` (Advanced Intrusion Detection Environment).
  ```bash
  sudo apt install aide
  sudo aideinit
  sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
  sudo aide --check
  ```

## Part 7. Encrypt Data at Rest (easy level)
Use `LUKS` (Linux Unified Key Setup) to encrypt a partition.
  ```bash
  sudo cryptsetup luksFormat /dev/sdX
  sudo cryptsetup luksOpen /dev/sdX encrypted_partition
  sudo mkfs.ext4 /dev/mapper/encrypted_partition
  sudo mount /dev/mapper/encrypted_partition /mnt
  ```

## Part 8. Regular Backups (easy level)

## VM creation 
```bash

multipass launch  docker --name ece --cpus 2 --memory 4g
```

```bash
multipass shell ece
```
installation of backup tool

```bash
sudo apt-get install restic
```

## creation of container environment

```bash

cat <<EOF >> ~/docker-compose.yml
version: '3.1'
services :
  db1:
    image: postgres:10-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: changeme
      POSTGRES_DB: tododb
  db2:
    image: postgres:10-alpine
    ports:
      - "5433:5433"
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: changeme
      POSTGRES_DB: tododb
  admin:
    image: adminer
    restart: always
    depends_on: 
      - db1
      - db2
    ports:
      - 8080:8080
  minio:
    image: quay.io/minio/minio
    container_name: minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: ROOTNAME
      MINIO_ROOT_PASSWORD: CHANGEME123
    volumes:
      - ~/minio/data:/data
    command: server /data --console-address ":9001"
EOF
```


```bash
docker-compose up -d
```

### Installation of mini storage object

```bash
curl https://dl.min.io/client/mc/release/linux-amd64/mc   --create-dirs   -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc


sudo cp $HOME/minio-binaries/mc /usr/local/bin/

mc --help

mc alias set minio http://localhost:9000 ROOTNAME CHANGEME123
```
#### bucket creation
```bash
mc mb myminio/test-bucket

```
#### key access creation

a faire la GUI de minio

#### creation of the Minio policy

```bash

cat <<EOF >> ~/policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::test-bucket/*"
    }
  ]
}
EOF

```bash
mc admin policy create minio test-policy policy.json

mc admin policy list minio

```


### repoing the restic tool


```bash

cat <<EOF >> ~/restic-env
export AWS_ACCESS_KEY_ID=9KqdKR65otUfqk0CiA7o
export AWS_SECRET_ACCESS_KEY=YilZ6HWY1LdChkKdQfFtHDs1NMEwvbTw1vWQaq8Y
export RESTIC_REPOSITORY="s3:http://localhost:9000/test-bucket"
export RESTIC_PASSWORD="cpi"
EOF
```

```bash
source ~/restic-env

echo $RESTIC_REPOSITORY


restic init
```
### populating the database

```bash
docker exec -it ubuntu_db1_1 psql -U user -d tododb -c " CREATE TABLE users ( id SERIAL PRIMARY KEY, name VARCHAR(50), email VARCHAR(50), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ); CREATE TABLE orders ( id SERIAL PRIMARY KEY, user_id INT REFERENCES users(id), product_name VARCHAR(100), price DECIMAL(10, 2), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ); "
```

```bash
docker exec -it ubuntu_db1_1 psql -U user -d tododb -c " INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com'), ('Jane Doe', 'jane@example.com'), ('Alice Smith', 'alice@example.com'), ('Bob Johnson', 'bob@example.com'); "

```

```bash
docker exec -it ubuntu_db1_1 psql -U user -d tododb -c " INSERT INTO orders (user_id, product_name, price) VALUES (1, 'Laptop', 1200.00), (1, 'Mouse', 25.00), (2, 'Smartphone', 800.00), (3, 'Keyboard', 45.00), (4, 'Monitor', 300.00); "
```


### container 1 sql database dump

```bash

docker exec -t ubuntu_db1_1 pg_dump -U  user -d tododb > ~/dump.sql
```

### backup with dump restic
```bash

restic --repo s3:http://localhost:9000/test-bucket  backup ~/dump.sql

restic snapshots
rm ~/dump.sql
```
### backup restoration

```bash
restic --repo s3:http://localhost:9000/test-bucket restore 09db447f --target ~/restore
```
### database restoration on container 2
```bash
docker exec -i ubuntu_db2_1 psql -U user -d tododb < ~/restore/home/ubuntu/dump.sql