# 0x0E. Web Stack Debugging #1 📡🛠️

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
    - [General](#general)
3. [Tasks](#tasks)
    - [0. Nginx likes port 80](#0-nginx-likes-port-80)
    - [1. Make it sweet and short](#1-make-it-sweet-and-short)
4. [Conclusion](#conclusion)
5. [Author](#author)

## Overview
Welcome to the Web Stack Debugging project! This project will help you enhance your debugging skills by tackling issues within a web stack environment. You will be working with Nginx, a popular web server, and ensuring it runs smoothly on an Ubuntu container.

## Requirements 📋

### General
- **Editors:** vi, vim, emacs
- **Operating System:** Ubuntu 20.04 LTS
- **File Requirements:** 
  - All files must end with a new line
  - A `README.md` file at the root of the project is mandatory
- **Script Requirements:**
  - All Bash scripts must be executable
  - All Bash scripts must pass Shellcheck without any error
  - All Bash scripts must run without error
  - The first line of all Bash scripts should be `#!/usr/bin/env bash`
  - The second line should be a comment explaining the script's purpose
  - Usage of `;`, `&&`, and `wget` is prohibited


## Tasks 🚀

### 0. Nginx likes port 80
**Objective:** Ensure that Nginx is running and listening on port 80 on all IPv4 IPs of the server.

**Steps:**
1. Debug the issue preventing Nginx from listening on port 80.
2. Write a Bash script to automate the fix.

**Script:** `0-nginx_likes_port_80`
```bash
#!/usr/bin/env bash
# Install and configure Nginx to listen on port 80
apt-get update
apt-get install -y nginx
sed -i 's/listen 80 default_server;/listen 80 default_server;/' /etc/nginx/sites-available/default
sed -i 's/listen \[::\]:80 default_server;/listen [::]:80 default_server;/' /etc/nginx/sites-available/default
service nginx start

1. Make it sweet and short 🍬✂️
Objective: Create a compact version of the previous script that is no longer than 5 lines.

Script: 1-debugging_made_short

#!/usr/bin/env bash
# Install, configure, and start Nginx
apt-get update
apt-get install -y nginx
sed -i 's/listen 80 default_server;/listen 80 default_server;/' /etc/nginx/sites-available/default
sed -i 's/listen \[::\]:80 default_server;/listen [::]:80 default_server;/' /etc/nginx/sites-available/default
service nginx start

Conclusion 🎯
By completing these tasks, you will have improved your debugging skills and gained more experience with configuring and managing web servers. This project challenges you to be concise, efficient, and thorough in your approach.

Author ✍️
Yusuf MM
