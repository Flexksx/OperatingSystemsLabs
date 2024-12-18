# Signal Handling in Python

This Python script demonstrates how to handle UNIX signals (`SIGUSR1` and `SIGUSR2`) using the `signal` module. Signals are a form of inter-process communication (IPC) used to notify a process of an event or interrupt its execution.

## Script Overview

- **`SIGUSR1` Handling**:  
  When the process receives the `SIGUSR1` signal, it triggers the `handle_sigusr1` function, which simply prints a message: `"SIGUSR1 received"`.

- **`SIGUSR2` Handling**:  
  When the process receives the `SIGUSR2` signal, it triggers the `handle_sigusr2` function, which:
  1. Generates a random alphanumeric string of 100 characters.
  2. Prints the random string to the console.
  3. Exits the program using `sys.exit(0)`.

- **Infinite Loop**:  
  The script runs an infinite loop, waiting to receive signals while keeping the process alive.

## Running the Script

1. Save the script in a file, e.g., `signal_handler.py`.
2. Run the script:
    ```bash
    python3 signal_handler.py
    ```
3. Find the process with:wq
    ```bash
    ps aux | grep signal_handler.py
    ```
4. Send signals to the running process:
   1. To send `SIGUSR1`:
        ```bash
        kill -SIGUSR1 <process_id>
        ```
   2. To send `SIGUSR2`:
        ```bash
        kill -SIGUSR2 <process_id>
        ```