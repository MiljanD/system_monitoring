import threading
import psutil
import re
from display_functions import display_usage
import time
import os


# Constants
BYTES_IN_GB = 1024 ** 3
TOTAL_MEMORY = round(psutil.virtual_memory().total / BYTES_IN_GB, 2)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    current_cpu_usage = psutil.cpu_percent()
    current_memory_usage = psutil.virtual_memory().percent

    display_usage(current_cpu_usage, current_memory_usage)
    time.sleep(1)

