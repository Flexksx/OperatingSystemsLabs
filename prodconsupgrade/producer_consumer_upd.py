import multiprocessing as mp
import random
import time
from datetime import datetime

# Configuration
NUM_PRODUCERS = 3
NUM_CONSUMERS = 3
MAX_PRODUCTION = 5  # Maximum items allowed in the queue at a time
MAX_CONSUMPTION = 2  # Maximum simultaneous consumers processing items


# Producer function
def producer(producer_id, queue, semaphore):
    while True:
        semaphore.acquire()  # Limit overproduction
        items = [random.randint(1, 100) for _ in range(3)]
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Producer {producer_id} produced items: {items}")
        queue.put((producer_id, items))  # Add items to the queue
        semaphore.release()
        time.sleep(random.uniform(1, 3))  # Simulate work


# Consumer function
def consumer(consumer_id, queue, semaphore):
    while True:
        semaphore.acquire()  # Limit simultaneous consumption
        try:
            producer_id, items = queue.get()  # Block until data is available
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Consumer {
                  consumer_id} consumed items from Producer {producer_id}: {items}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate work
        finally:
            semaphore.release()  # Ensure semaphore is released


if __name__ == "__main__":
    # Create shared resources
    # Queue for producer-consumer communication
    queue = mp.Queue(MAX_PRODUCTION)
    producer_semaphore = mp.Semaphore(
        MAX_PRODUCTION)  # Limit items in the queue
    consumer_semaphore = mp.Semaphore(
        MAX_CONSUMPTION)  # Limit active consumers

    # Start producers
    producers = [
        mp.Process(target=producer, args=(i, queue, producer_semaphore))
        for i in range(NUM_PRODUCERS)
    ]
    for p in producers:
        p.start()

    # Start consumers
    consumers = [
        mp.Process(target=consumer, args=(i, queue, consumer_semaphore))
        for i in range(NUM_CONSUMERS)
    ]
    for c in consumers:
        c.start()

    try:
        # Wait for processes to finish (they won't in this infinite example)
        for p in producers:
            p.join()
        for c in consumers:
            c.join()
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
        for p in producers:
            p.terminate()
        for c in consumers:
            c.terminate()
