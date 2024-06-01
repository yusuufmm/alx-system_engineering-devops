# 0x0B. SSH 🔒

## Background Context 📚

In this project, I was assigned an Ubuntu server located in a remote datacenter. My task was to connect to this server using SSH, not with a password, but with an RSA key. The server was pre-configured with the public key I had created in a previous project.

To access my server details, I used the "my servers" section of our intranet, which provided the IP and username for SSH connections.

**Note:** The server runs on Ubuntu 20.04 LTS.

## Requirements 📋

Throughout this project, I adhered to the following requirements:

- **Allowed editors:** `vi`, `vim`, `emacs`
- **Scripts interpreted on:** Ubuntu 20.04 LTS
- **All files end with a new line**
- **README.md file is mandatory** at the root of the project folder
- **All Bash scripts are executable**
- **First line of all Bash scripts:** `#!/usr/bin/env bash`
- **Second line of all Bash scripts:** A comment explaining the script's purpose

## Task Overview 📝

Here's a brief overview of the tasks I completed:

```bash
# 0. Use a Private Key 🔐
# I wrote a Bash script to connect to my server using the private key ~/.ssh/school with the user ubuntu.
# This script uses ssh single-character flags exclusively.

# 1. Create an SSH Key Pair 🔑
# I created a Bash script to generate an RSA key pair named 'school' with 4096 bits, secured by the passphrase 'betty'.

# 2. Client Configuration File ⚙️
# I configured my SSH client to use the private key ~/.ssh/school and ensured it refuses password authentication.
