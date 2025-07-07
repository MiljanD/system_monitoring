import threading
import time
import psutil
import sys
import os

# Constants
BYTES_IN_GB = 1024 ** 3
TOTAL_MEMORY = round(psutil.virtual_memory().total / BYTES_IN_GB, 2)
LABEL_WIDTH = 15
USAGE_ROW = 7
PROCESS_ROW = 12
INPUT_ROW = 9

# deljene globalne promenjiva
sort_key = "cpu_percent"
sort_key_lock = threading.Lock()
display_paused = False
display_lock = threading.Lock()
running = True


def display_usage(bars=20):
    global running
    while running:
        cpu_usage = psutil.cpu_percent()
        mem_data = psutil.virtual_memory()

        cpu_usage_percentage = cpu_usage / 100
        cpu_bar = "█" * int(cpu_usage_percentage * bars) + "-" * (bars - int(cpu_usage_percentage * bars))

        memory_usage_percentage = mem_data.percent / 100
        memory_bar = "█" * int(memory_usage_percentage * bars) + "-" * (bars - int(memory_usage_percentage * bars))
        available_memory = ((mem_data.available / BYTES_IN_GB) / TOTAL_MEMORY) * 100
        print(f"\033[{USAGE_ROW};1H", end="")
        print(f"{'CPU Usage:'.ljust(LABEL_WIDTH)} |{cpu_bar}| {str(f'{cpu_usage:.2f}%').rjust(6)}  "
              f"{'Memory Usage:'.ljust(LABEL_WIDTH)} |{memory_bar}| {str(f'{memory_usage_percentage *100 :.2f}%').rjust(6)}  "
              f"{'Available Memory:'.ljust(LABEL_WIDTH)} {str(f'{available_memory:.2f}%').rjust(6)}", end="", flush=True)

        print(f"\033[{INPUT_ROW +1};1H", end="", flush=True)
        time.sleep(1)


def display_processes(limit=5):
    global running
    while running:
        time.sleep(5)
        global sort_key

        with sort_key_lock:
            current_key = sort_key
            processes = list(psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]))
            for proces in processes:
                proces.cpu_percent(interval=0.0)

            time.sleep(1)

            list_of_processes = []
            for proces in processes:
                try:
                    list_of_processes.append(proces.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            sorted_processes = sorted(list_of_processes, key=lambda p:p[current_key], reverse=True)

            for i in range(limit + 3):
                print(f"\033[{PROCESS_ROW + i};1H\033[K", end="")

            print(f"\033[{PROCESS_ROW};1H", end="")
            print(f"{'PID'.ljust(8)} "
                  f"{'Name'.ljust(25)}"
                  f"{'CPU %'.rjust(10)}"
                  f"{'RAM %'.rjust(10)}")

            print(f"\033[{PROCESS_ROW +1};2H", end="")
            print("-" * 53)


            print(f"\033[{PROCESS_ROW + 2};1H\033[K", end="")

            for i, proc in enumerate(sorted_processes[:limit]):
                print(f"\033[{PROCESS_ROW + 2 + i};1H", end="")

                cpu = proc["cpu_percent"]
                mem = proc["memory_percent"]

                if cpu > 50:
                    color = "\033[91m"
                elif mem > 20:
                    color = "\033[93m"
                else:
                    color = "\033[97m"

                reset = "\033[0m"

                print(f"{color}"
                    f"{str(proc['pid']).ljust(8)}"
                    f"{proc['name'][:25].ljust(25)}"
                    f"{str(f'{cpu:.1f}').rjust(10)}"
                    f"{str(f'{mem:.1f}').rjust(10)}"
                      f"{reset}")

        print(f"\033[{INPUT_ROW + 1 };1H", end="", flush=True)


def listen_for_input():
    global sort_key
    global running

    while running:
        print(f"\033[{INPUT_ROW};1H\033[K", end="")
        sys.stdout.write(f"\033[{INPUT_ROW};1H\033[KEnter sorting key (for CPU enter 1/for RAM enter 2/for Name enter 3): ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip().lower()

        print(f"\033[{INPUT_ROW + 1};1H\033[K", end="")

        with sort_key_lock:
            if user_input in ("exit", "x"):
                running = False
                os.system("cls")
                print(f"\033[1;1H\033[91mExiting...Goodbye!\033[0m")
                break
            elif user_input == "1":
                    sort_key = "cpu_percent"
            elif user_input == "2":
                    sort_key = "memory_percent"
            elif user_input == "3":
                    sort_key = "name"
            else:
                print(f"\033[{INPUT_ROW + 1 };1H\033[K", end="")
                print(f"\033[{INPUT_ROW + 1 };1HUnknown command, try again.")
                time.sleep(1)


        print(f"\033[{INPUT_ROW};1H\033[K", end="")
        print(f"\033[{INPUT_ROW + 1};1H\033[K", end="")






