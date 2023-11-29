Web Stack Debugging Project 0 - "Give me a page!"

Hello and welcome to the Web Stack Debugging journey! In this project, we'll embark on a mission to revive Apache on a Docker container and have it happily greet us with a "Hello Holberton." Get ready for some debugging magic!

## Requirements 🛠️

- **Editors:** vi, vim, emacs
- **Environment:** Ubuntu 14.04 LTS
- **File Endings:** All files should end with a new line
- **README.md:** A mandatory guide to your project
- **Executable Scripts:** All Bash scripts must be executable
- **Shellcheck:** Ensure your scripts pass Shellcheck without any errors
- **Execution:** Bash scripts must run without error
- **Shebang Line:** The first line of your Bash scripts should be exactly `#!/usr/bin/env bash`
- **Script Comment:** The second line of your Bash scripts should be a comment explaining the script's purpose

## Task 0: Give me a page! 🚀

In this inaugural debugging mission, we'll tackle the challenge of making Apache run on a Docker container and respond with a delightful "Hello Holberton" when queried at its root.

### Example:

1. Launch the Docker container:

    ```bash
    docker run -p 8080:80 -d -it holbertonschool/265-0
    ```

2. Confirm the container is ready:

    ```bash
    docker ps
    ```

3. Curl the port 8080 and encounter the dreaded `curl: (52) Empty reply from server` error.

4. Dive into the container for hands-on debugging:

    ```bash
    docker exec -it <container_id> /bin/bash
    ```

5. Work your magic within the container. Fix whatever needs fixing to bring back the warm "Hello Holberton."

6. Test your superhero fixes:

    ```bash
    curl 0:8080
    ```

    Now, it should greet you warmly!

## Share Your Wisdom 🌟
