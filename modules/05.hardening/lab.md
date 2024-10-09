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

## Part 4. SSH Key Authentication (easy level)
Generate SSH keys and disable password authentication.
  ```bash
  ssh-keygen -t rsa -b 4096
  ssh-copy-id user@server
  sudo nano /etc/ssh/sshd_config
  # Set PasswordAuthentication to no
  sudo systemctl restart sshd
  ```

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

multipass launch  docker --name ece --cpus 2 --memory 4g  --network name=virbr0,mode=auto
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