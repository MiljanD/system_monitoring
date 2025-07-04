import threading
import psutil
import re
from display_functions import display_usage
import time
import os


while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    current_cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()

    display_usage(current_cpu_usage, memory_info)
    time.sleep(1)

