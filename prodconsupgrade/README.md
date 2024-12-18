# Producer-Consumer System Using Multiprocessing

This Python script implements a **Producer-Consumer** model using the `multiprocessing` module. The system demonstrates inter-process communication through a shared `Queue` with semaphores to manage concurrency and prevent resource contention.

## Key Features

1. **Producers**:
   - Generate random items (three integers between 1 and 100) and add them to a shared queue.
   - Use a semaphore to limit overproduction, ensuring the queue does not exceed its maximum capacity.

2. **Consumers**:
   - Retrieve items from the queue and simulate processing them.
   - Use a semaphore to control the number of simultaneous consumers processing items.

3. **Shared Resources**:
   - **Queue**: Acts as the communication channel between producers and consumers. Configured with a maximum capacity (`MAX_PRODUCTION`).
   - **Semaphores**: Used to manage the number of items in the queue and the number of active consumers.

4. **Concurrency Management**:
   - Producers and consumers run as independent processes.
   - Semaphores ensure the queue is neither overfilled nor over-consumed.

## Configuration Parameters

| Parameter         | Description                                     | Value |
| ----------------- | ----------------------------------------------- | ----- |
| `NUM_PRODUCERS`   | Number of producer processes                    | 3     |
| `NUM_CONSUMERS`   | Number of consumer processes                    | 3     |
| `MAX_PRODUCTION`  | Maximum items allowed in the queue at a time    | 5     |
| `MAX_CONSUMPTION` | Maximum simultaneous consumers processing items | 2     |

## Workflow

1. **Producers**:
   - Acquire a semaphore to check if there is space in the queue.
   - Generate items and add them to the queue.
   - Release the semaphore to signal availability for more production.

2. **Consumers**:
   - Acquire a semaphore to check if consumption is allowed.
   - Retrieve items from the queue and process them.
   - Release the semaphore after processing.

3. **Main Process**:
   - Initializes the shared queue and semaphores.
   - Starts producer and consumer processes.
   - Listens for keyboard interruption (`Ctrl+C`) to terminate all processes gracefully.

## Running the Script

1. Save the script to a file, e.g., `producer_consumer_upd.py`.
2. Run the script:
   ```bash
   python3 producer_consumer_upd.py
   ```
3. Observe the real-time interactions between producers and consumers in the terminal.
### Example output
```
[12:00:01] Producer 0 produced items: [23, 45, 67]
[12:00:02] Consumer 0 consumed items from Producer 0: [23, 45, 67]
[12:00:03] Producer 1 produced items: [12, 34, 56]
[12:00:04] Consumer 1 consumed items from Producer 1: [12, 34, 56]
...
```
### Graceful Shutdown
The script handles KeyboardInterrupt (Ctrl+C) gracefully by terminating all producer and consumer processes.
