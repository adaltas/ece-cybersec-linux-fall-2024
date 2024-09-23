---
duration: 1h
---

# Lab: To get started

setting up the environment for future labs

## Objectives

- deploy 2 vm ubunutu
- Deploying vm multipass
- Honeypot

## Tasks

1. Part 1. Deploying ubunutu vm (easy level)
2. Part 2. Deploying vm multipass (easy level)
3. Part 3. Honeypot Lab (easy level)

## Prerequisites

Have a hypervisor installed and operational 

## Part 1. Deploying ubunutu vm (easy level)

For VM creation download the[`iso ubuntu`](https://releases.ubuntu.com/jammy/)

## Part 2. Deploying vm multipass (easy level)

For install [`multipass`](https://multipass.run/install)

## Part 3. Honeypot Lab (easy level)

Here is an example of a **Honeypot Lab** you can follow to set up a basic Honeypot on a virtual machine (VM) using Multipass and the Honeypot tool **Cowrie**. **Cowrie** is an interactive Honeypot that simulates an SSH and Telnet server to attract attackers and capture their actions without compromising the real system.

### Lab Objective:
1. Install a Honeypot (Cowrie) on a VM.
2. Monitor and record intrusion attempts.
3. Analyze the data collected by the Honeypot.

### Prerequisites:
- Have **Multipass** installed on your machine.
- Have an active internet connection to install dependencies on the VM.
- Basic knowledge of SSH and networks.

### Create a VM with Multipass

Open a terminal on your host machine and run the following command to create a VM with Multipass:

```bash
multipass launch --name honeypot-vm --memory 1G --disk 5G --cpus 1
 ```
   - `--name honeypot-vm`: The name of the VM.
   - `--mem 1G`: Assigns 1 GB of RAM to the VM.
   - `--disk 5G`: Assigns 5 GB of disk space.
   - `--cpus 1`: Assigns 1 CPU.

Access the VM:

```bash
multipass shell honeypot-vm
```

### Install Dependencies

Once inside the VM, install the required packages for Cowrie:

```bash
sudo apt update
sudo apt install -y git python3-virtualenv python3-dev libssl-dev libffi-dev build-essential
```

### Download and Install Cowrie

Clone the Cowrie repository:

```bash
git clone https://github.com/cowrie/cowrie
cd cowrie
```

Create a Python virtual environment:

```bash
virtualenv --python=python3 cowrie-env
source cowrie-env/bin/activate
```

Install Python dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Configure Cowrie

Copy the sample configuration file to customize it:

```bash
cp etc/cowrie.cfg.dist etc/cowrie.cfg
```

Open the configuration file using a text editor like **nano**:

```bash
nano etc/cowrie.cfg
```

In this file, you can configure several options such as:
- The SSH port to use (Cowrie defaults to running a fake SSH server on port 2222).
- The Telnet port (if you want to capture Telnet connections as well).
- Log management.

### Step 5: Start the Honeypot

Activate the Python virtual environment:

```bash
source cowrie-env/bin/activate
```

Start Cowrie:

```bash
bin/cowrie start
```

Cowrie is now running a fake SSH server on port 2222.

### Step 6: Test the Honeypot

To test your Honeypot, try an SSH connection to port 2222 on the VM from the host (replace `vm_ip` with the IP address of the VM obtained via `multipass list`):

```bash
ssh -p 2222 root@vm_ip
```

Run a few commands to see how Cowrie logs the actions.

### Step 7: Analyze the Data

1. The logs of recorded attacks can be found in the `log` directory of Cowrie. To access it:

```bash
cat var/log/cowrie/cowrie.log
```

2. You can analyze the logs to see login attempts and the commands executed by attackers.

