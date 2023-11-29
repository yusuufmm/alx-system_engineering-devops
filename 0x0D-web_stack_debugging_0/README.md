# Web Stack Debugging 0 - Debugging Docker Container

Welcome to the world of debugging! In this project, we're on a mission to fix Apache in a Docker container. Our goal is to make it return a page with the greeting "Hello Holberton" when we query its root. Let's dive in!

## Requirements

- **Environment:** Ubuntu 14.04 LTS
- **Allowed Editors:** vi, vim, emacs
- **File Endings:** Ensure all files end with a new line.
- **README.md:** Mandatory guide to the project.
- **Executable Scripts:** All Bash scripts must be executable.
- **Shellcheck:** Scripts should pass Shellcheck without errors.
- **Shebang Line:** Start Bash scripts with `#!/usr/bin/env bash`.
- **Script Comment:** Add a comment on the second line explaining the script's purpose.

## Tasks

### 0. Give me a page!

#### Objective
Make Apache run on a Docker container and return a page containing "Hello Holberton" when querying its root.

#### Steps
1. Launch the Docker container using the provided image: `holbertonschool/265-0`.
2. Map port 8080 on the host to port 80 on the container.
3. Run the container in detached mode.
4. Diagnose the issue by checking the container's status (`docker ps`) and using `curl` to query the container at `0:8080`.
5. Debug inside the container using `docker exec -it <container_id> /bin/bash`.
6. Fix whatever is preventing Apache from working.
7. Test the fix using `curl`.

#### Submission
Provide the commands used to fix the issue in the answer file. Share your wisdom by updating the README.md in your GitHub repository.

## Let's Get Debugging!
Your mission, should you choose to accept it, is to debug and conquer! 🚀

**By:** YUSUF MM
