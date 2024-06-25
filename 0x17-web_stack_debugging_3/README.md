tack Debugging #3 🐞🔧

Welcome to the Web Stack Debugging #3 project! This project focuses on debugging a WordPress website running on a LAMP stack. 🌐✨

## Task 0: Strace is your Friend 🕵️‍♂️💻

### Objective
Use `strace` to find out why Apache is returning a 500 error. Fix the issue and automate the solution using Puppet.

### Steps
1. **Identify the Issue with `strace`**:
    - Find the Apache process ID:
          ```bash
                ps aux | grep apache2
                      ```
                          - Attach `strace` to the Apache process:
                                ```bash
                                      strace -p PID -f -o strace.log
                                            ```
                                                - Trigger the 500 error:
                                                      ```bash
                                                            curl -sI 127.0.0.1
                                                                  ```
                                                                      - Analyze `strace.log` to find the issue.

                                                                      2. **Fix the Issue**:
                                                                          - Create a Puppet manifest `0-strace_is_your_friend.pp` to automate the fix.

