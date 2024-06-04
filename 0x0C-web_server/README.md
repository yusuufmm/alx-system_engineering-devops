# 0x0C. Web Server 🌐

## Background Context 📚

This project was an exploration into the configuration and management of web servers, specifically focusing on automating tasks to ensure smooth and efficient server operation. The tasks aimed to teach the importance of scripting for automation, which is crucial for handling large-scale server environments. The project took place from May 6, 2024, to May 8, 2024.

## Requirements 📋

Throughout this project, the following requirements were essential:

- **Allowed editors:** vi, vim, emacs
- **All files will be interpreted on:** Ubuntu 16.04 LTS
- **All files should end with a new line**
- **A `README.md` file at the root of the project folder is mandatory**
- **All Bash scripts must be executable**
- **Bash scripts must pass Shellcheck (version 0.3.7) without any error**
- **First line of all Bash scripts:** `#!/usr/bin/env bash`
- **Second line of all Bash scripts:** A comment explaining what the script does
- **Cannot use `systemctl` for restarting a process**

## Learning Objectives 🎓

By the end of this project, I was able to explain:

- The main role of a web server
- The concept of child processes and their importance in web servers
- Key HTTP requests and their functions
- The role of DNS and its various record types (A, CNAME, TXT, MX)

## Task Overview 📝

Here’s a summary of the tasks I tackled:

```bash
# 0. Transfer a file to your server 🔄
# A Bash script to securely transfer files to a server using SCP.

# 1. Install Nginx web server 🌐
# A script to install and configure Nginx, ensuring it serves a "Hello World!" page.

# 2. Setup a domain name 🌍
# Configuring a DNS record to link a domain to the server.

# 3. Redirection 🔀
# Configuring Nginx to redirect requests from one URL to another.

# 4. Not found page 404 🚫
# Customizing the 404 error page to return a specific message.

# 5. Install Nginx web server (w/ Puppet) 🛠️
# Using Puppet to automate the installation and configuration of Nginx.
