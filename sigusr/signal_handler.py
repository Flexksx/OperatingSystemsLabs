import signal
import random
import string
import sys


def handle_sigusr1(signum, frame):
    print("SIGUSR1 received")


def handle_sigusr2(signum, frame):
    random_string = ''.join(random.choices(
        string.ascii_letters + string.digits, k=100))
    print(random_string)
    sys.exit(0)


signal.signal(signal.SIGUSR1, handle_sigusr1)
signal.signal(signal.SIGUSR2, handle_sigusr2)

print("Program running, send SIGUSR1 or SIGUSR2 to test")
while True:
    pass
