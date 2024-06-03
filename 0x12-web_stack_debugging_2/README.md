# 0x12. Web Stack Debugging #2 🐛

## Background Context 📚

In this project, I delved into the intricacies of web stack debugging. The tasks were designed to simulate real-world scenarios where servers need to be configured securely and run efficiently. The project spanned from May 27, 2024, to May 29, 2024, giving me a hands-on opportunity to troubleshoot and optimize server behavior.

## Requirements 📋

Throughout this project, I ensured to meet the following requirements:

- **All files will be interpreted on:** Ubuntu 20.04 LTS
- **All files should end with a new line**
- **A `README.md` file at the root of the project folder is mandatory**
- **All Bash scripts must be executable**
- **Bash scripts must pass Shellcheck without any error**
- **Bash scripts must run without error**
- **First line of all Bash scripts:** `#!/usr/bin/env bash`
- **Second line of all Bash scripts:** A comment explaining what the script does

## Task Overview 📝

Here's a brief overview of the tasks I tackled:

```bash
# 0. Run software as another user 🔄
# I wrote a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument.
# This helps understand how to safely execute commands as different users.

# 1. Run Nginx as Nginx 🌐
# The goal was to ensure Nginx runs as the less privileged 'nginx' user instead of root.
# This enhances security by limiting the impact of potential breaches.

# 2. 7 lines or less ✂️
# Using the solution from task #1, I condensed the fix to a Bash script with 7 lines or fewer.
# This was a challenge in writing efficient and concise code.
