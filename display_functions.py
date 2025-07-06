import threading
import time
import psutil
import sys

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


def display_usage(bars=20):
    while True:
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

        print(f"\033[{INPUT_ROW};33H", end="", flush=True)
        time.sleep(1)


def display_processes(limit=5):
    while True:
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

            print(f"\033[{PROCESS_ROW +1};1H", end="")
            print("-" * 53)


            print(f"\033[{PROCESS_ROW + 2};1H\033[K", end="")

            for i, proc in enumerate(sorted_processes[:limit]):
                print(f"\033[{PROCESS_ROW + 2 + i};1H", end="")

                print(f"{str(proc['pid']).ljust(8)}"
                    f"{proc['name'][:25].ljust(25)}"
                    f"{str(f'{proc['cpu_percent']:.1f}').rjust(10)}"
                    f"{str(f'{proc['memory_percent']:.1f}').rjust(10)}")

        print(f"\033[{INPUT_ROW};33H", end="", flush=True)


def listen_for_input():
    global sort_key

    while True:
        print(f"\033[{INPUT_ROW};1H\033[K", end="")
        sys.stdout.write(f"\033[{INPUT_ROW};1H\033[KEnter sorting key (CPU/RAM/Name): ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip().lower()

        print(f"\033[{INPUT_ROW + 1};1H\033[K", end="")

        with sort_key_lock:
            if user_input == "cpu":
                    sort_key = "cpu_percent"
            elif user_input == "mem":
                    sort_key = "memory_percent"
            elif user_input == "name":
                    sort_key = "name"
            else:
                print(f"\033[{INPUT_ROW +1 };1H\033[K", end="")
                print("Unknown command, try again.")


        print(f"\033[{INPUT_ROW};1H\033[K", end="")
        print(f"\033[{INPUT_ROW + 1};1H\033[K", end="")






