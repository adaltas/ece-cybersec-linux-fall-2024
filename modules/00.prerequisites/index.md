# Prerequisites

## Linux Environment

If Mac OS or Windows, Install the following software on your computer:
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for Windows and x86 archictures.
- [MultiPass](https://multipass.run/docs/install-multipass) for MacOS and arm64 archictures.

If you already have native or virtual Linux OS, jump to the "common tools" section.

### VirtualBox

Form the VirtualBox interface, create a new VM with:

- At least 4GiB, 8GiB recommended.
- At least 2 cpus, 4 CPUs recommended.

Use last Ubuntu, or your favorite distribution (not supported).

### Multipass

Install multipass using HomeBrew.

```bash
brew install bash-completion
brew install --cask multipass
multipass launch \
  --name ece \
  --cpus 4 \
  --memory 8G \
  --disk 60G
multipass exec ece -- \
  sudo bash -c "echo 'DNS=8.8.8.8' >> /etc/systemd/resolved.conf"
multipass exec ece -- \
  sudo systemctl restart systemd-resolved
```

## Common tools

### Git

Git is commonly [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) with the system package manager with your [account information](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

```bash
apt install -y git
git config --global user.name "<first_name> <last_name>"
git config --global user.email "<email>"
```

### Docker

The [installation procedure](https://docs.docker.com/engine/install/ubuntu/) for the official recommandation.

```bash
# Install packages
sudo apt update
sudo apt install ca-certificates curl gnupg
# Add Docker’s official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
# Set up the repository
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
# Install Docker Engine
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# Linux post install
sudo usermod -aG docker $USER
newgrp docker
```

### Terminal

- Most useful developer tool
- Any number of customizations
- On Windows: Linux Bash Shell, Git Bash (don't use default CMD, or PowerShell, ever, in your life!)
- On macOS / Linux: native Terminal

### Bash

Learn Bash base commands:
- [Bash base commands](https://www.educative.io/blog/bash-shell-command-cheat-sheet)
- [GameShell: a "game" to teach the Unix shell](https://github.com/phyver/GameShell)

### Zsh

Zsh (Z shell) is a powerful Unix shell that offers advanced features, such as programmable command-line completion, a rich scripting language, and extended customization options, making it a popular choice for power users.

```bash
# Install Zsh
sudo apt install -y zsh
# Set Zsh as your default shell
chsh -s $(which zsh)
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Note, `.profile` is not automatically sourced:

```bash
echo ". ~/.profile" >> ~/.zshrc
```

### Vi(m)

Vim is a **modal text editor**
No insertion per default! Need to enter insertion mode.

- Use `i` to enter edit mode and `ESC` to exit it
- Use `:` to enter command mode
  - `w` to write file
  - `q` to quit
  - `q!` to quit without saving
  - 'x' to write & quit
- Use `/` to search for text
- `vimtutor` is the best tutorial to learn

## Communities

- [HackerNews](https://news.ycombinator.com/)
  - Most qualified community
  - Large technological scope coverage
- [StackOverflow](https://stackoverflow.com/)
  - Huge data source
  - Reactive community
  - Any subject
  - Lots of answered questions (> 1M !)
  - Don’t forget the source code!
- [Dev.to](https://dev.to/), [Medium](https://medium.com/), ...
  - Blog publications
