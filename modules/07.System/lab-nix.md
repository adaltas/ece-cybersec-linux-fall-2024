---
duration: 1h
---

# Using the Nix package manager on Ubuntu

Nix is a package manager that provides reproducible and isolated environments for software development, ensuring consistent builds and deployments. It allows users to manage dependencies and configurations in a declarative way, making it easier to maintain and share development environments across different systems.

## Requirements

Enter the Ubuntu machine. The `nixuser` account used in the lab is created with passwordless sudoer privileges.

```bash
# On MacOS with multipass
multipass shell ece
# User creation
sudo useradd -m -s /bin/bash -G sudo nixuser
# Passwordless sudo privilege
echo "nixuser ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/nixuser
# New shell session
sudo su - nixuser
```

The `-m` flag create the user's home directory, the `-s` flag set the default shell, and the `-G` flag provide group memberships.

The nix package manager is installed with support for the new nix commands and flakes.

```bash
sh <(curl -L https://nixos.org/nix/install) --daemon
sudo su - nixuser
mkdir -p ~/.config/nix/
cat <<NIX >~/.config/nix/nix.conf
extra-experimental-features = nix-command flakes
NIX
```

## First steps with Nix

Flakes are a new feature in Nix that provide a standardized way to define and manage Nix packages, projects, and environments in a more reproducible and user-friendly manner. The nixpkgs flake is a special flake that represents the entire Nix Packages collection, offering access to a vast repository of software packages.

List all packages in the nixpkgs flake (only the last 20 packages are printed).

```bash
nix search nixpkgs ^ | tail -20
```

Search for packages containing git and either frontend or gui. The `-e` flag hide the matching patterns.

```bash
nix search nixpkgs git 'frontend|gui'
```
A package


Using `nix run` allows the execution of applications in isolated environments, preventing pollution of your global system and ensuring clean, conflict-free operations. Run the `cowsay` command with arguments.

```bash
nix run nixpkgs#cowsay hello world!
```

Pipe `curl` stdout to Nix and jq

```bash
curl -s https://api.github.com/users/adaltas \
  | nix run nixpkgs#jq '.avatar_url' \
  | xargs curl \
  | nix run nixpkgs#ascii-image-converter -- - -C -H 40
```

## `nix shell`

Nix shell provides a reproducible and isolated environment for running software, ensuring that all dependencies and versions are exactly as specified. This is particularly useful for developers who need to work on projects with different or conflicting dependencies, as it allows them to create a clean, controlled environment without affecting the system-wide configuration. By using the Nix package manager, the Nix shell ensures that the software environment can be consistently replicated across different machines, enhancing portability and reducing “it works on my machine” issues.

We use `nix shell` to install the Redis client, run `redis-cli` to enter the REPL.

```bash
# Ensure the command is not installed
which redis-cli
# Install the command
nix shell nixpkgs#redis
# Execute the command
which redis-cli
/nix/store/<random>-redis-<version:7.2.5>/bin/redis-cli
# Enter a new session
sudo su - nixuser
# Redis client is not available
which redis-cli
# Exit and go back to the previous session
exit
# Redis client is present again
which redis-cli
/nix/store/<random>-redis-<version:7.2.5>/bin/redis-cli
```

## Home Manager

[Home Manager](https://nix-community.github.io/home-manager/index.xhtml) is a tool that allows you to declaratively manage your user environment, including your personal configurations and packages, using the Nix package manager.

The installation follows the [official instructions](https://nix-community.github.io/home-manager/index.xhtml#sec-install-standalone).

```bash
nix-channel --add https://github.com/nix-community/home-manager/archive/master.tar.gz home-manager
nix-channel --update
nix-shell '<home-manager>' -A install
cat ~/.config/home-manager/home.nix 
```

The default configuration file is located in `~/.config/home-manager/home.nix`. Edit the file to activate the Emacs text editor.

```nix
{ config, pkgs, ... }:
{
  ...
  programs.emacs.enable = true;
}
```

The `home-manager switch` command activate the new configuration.

```bash
# Emacs is not yet installed
which emacs
# The build command is optional before switch
home-manager build
# Build and activate configuration
home-manager switch
# Emacs is now installed
which emacs
/home/nixuser/.nix-profile/bin/emacs
```

Others settings may apply beside the `enable` property. Zsh is a powerful, customizable Unix shell, and Oh My Zsh is a popular framework for managing Zsh configurations, offering themes and plugins to enhance the shell experience.

```nix
{ config, pkgs, ... }:
{
  ...
  programs.zsh = {
    enable = true;
  };
  programs.zsh.oh-my-zsh = {
    enable = true;
    plugins = [ "git" "sudo" "docker" "kubectl" ];
    theme = "robbyrussell";
  };
}
```

Running the `zsh` command launches the Zsh shell, providing an interactive terminal environment with Zsh’s enhanced features and capabilities.

```bash
home-manager switch
zsh
```

## Configuration versioning

Home manager provides the tools to initialize your customized work environment within minites. Customizing the Git config is essential for tailoring Git’s behavior to your workflow, enabling personalized settings like aliases, commit templates, and user information for more efficient and consistent version control.

```nix
{ config, pkgs, ... }:
{
  ...
  programs.git = {
    enable = true;
    userName  = "wdavidw";
    userEmail = "david@adaltas.com";
    aliases = {
      lgb = "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%n' --abbrev-commit --date=relative --branches";
    };
    extraConfig = {
      core = {
        editor = "/usr/bin/vim";
      };
      init = {
        defaultBranch = "main";
      };
      pull = {
        rebase = true;
      };
      # https://git-scm.com/docs/git-rerere
      # Recording conflicted automerge results and corresponding hand resolve
      # results on the initial manual merge, and applying previously recorded
      # hand resolutions to their corresponding automerge results.
      rerere = {
        enabled = 1;
      };
    };
  };
}
```

Once your Nix configuration files are created, you can version them with Git, enabling a reproducible environment that can be easily deployed across all your machines.

```bash
# Activate the Git configuration
home-manager switch
# Git is configured
git config --list | cat
# Commit the Nix configuration
cd ~/.config/
git init
git add nix/nix.conf home-manager/home.nix
git commit -m 'feat: initial nix configuration'
```

## Additionnal resources

- [Home Manager Manual](https://nix-community.github.io/home-manager/index.xhtml)
- [My Nix Journey - Use Nix on Ubuntu ](https://tech.aufomm.com/my-nix-journey-use-nix-with-ubuntu/)
- [Install and Use Nix Package Manager on non-Nix OS like Ubuntu](https://itsfoss.com/ubuntu-install-nix-package-manager/)
