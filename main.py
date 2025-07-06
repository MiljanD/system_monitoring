import threading
import psutil
import re
from display_functions import display_usage, display_processes, listen_for_input
import time
import os



usage_thread = threading.Thread(target=display_usage, daemon=True)
usage_thread.start()

input_thread = threading.Thread(target=listen_for_input, daemon=True)
input_thread.start()

process_thread = threading.Thread(target=display_processes, args=(10,), daemon=True)
process_thread.start()



while True:
    time.sleep(1)



