
# Entry point for the terminal-based system monitor application

import threading
import display_functions
from display_functions import display_usage, display_processes, listen_for_input
import time


# Start the thread responsible for displaying CPU and memory usage

usage_thread = threading.Thread(target=display_usage, daemon=True)
usage_thread.start()

# Start the thread responsible for handling user input (sorting and exit)

input_thread = threading.Thread(target=listen_for_input, daemon=True)
input_thread.start()


# Start the thread responsible for displaying active processes
# The argument '10' sets the number of processes to display

process_thread = threading.Thread(target=display_processes, args=(10,), daemon=True)
process_thread.start()

# Keep the main thread alive while the application is running
# This loop checks the shared 'running' flag from display_functions

while display_functions.running:
    time.sleep(1)
