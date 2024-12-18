# Multiprocessing Producer-Consumer Model with Named Pipe

## Overview

This Python script implements a **Producer-Consumer model** using:
- **Multiprocessing** for managing multiple producers and consumers.
- **Named pipes** (FIFO) for inter-process communication.
- **Semaphores** to limit overproduction and simultaneous processing.

Producers write data to a named pipe, while consumers read and process the data.

---

## Key Features

1. **Producers**:
   - Generate random items (3 integers between 1 and 100).
   - Write data to the named pipe in the format: `producer_id:[item1, item2, item3]`.
   - Controlled by a semaphore to limit simultaneous production.

2. **Consumers**:
   - Continuously read data from the named pipe.
   - Process the received data, simulating a workload.
   - Controlled by a semaphore to limit the number of active consumers.

3. **Named Pipe**:
   - Acts as the shared communication medium between producers and consumers.
   - Ensures data flow in a synchronized manner.

4. **Concurrency**:
   - Multiple producers and consumers run as separate processes.

5. **Graceful Handling**:
   - Ensures the named pipe is created only if it doesn’t already exist.
   - Utilizes semaphores to prevent race conditions.

---

## Code Behavior

1. **Producers**:
   - Each producer generates a batch of random integers.
   - The producer writes its output to the named pipe, simulating a time delay for production.

2. **Consumers**:
   - Each consumer reads a line from the named pipe.
   - Decodes and processes the data, simulating a workload.

3. **Named Pipe**:
   - The script ensures the named pipe exists before starting processes.

---

## Example Output

```plaintext
[12:00:01] Producer 0 produced items: [23, 45, 67]
[12:00:02] Consumer 0 consumed items from Producer 0: [23, 45, 67]
[12:00:03] Producer 1 produced items: [12, 34, 56]
[12:00:04] Consumer 1 consumed items from Producer 1: [12, 34, 56]
```

## Configuration
* Pipe name `/tmp/producer_consumer_pipe`
* Semaphore limits: 
  * Producer - 3 concurrent processes
  * Consumer - 5 concurrent processes
