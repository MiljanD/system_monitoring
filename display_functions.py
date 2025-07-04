import psutil

# Constants
BYTES_IN_GB = 1024 ** 3
TOTAL_MEMORY = round(psutil.virtual_memory().total / BYTES_IN_GB, 2)
LABEL_WIDTH = 15


def display_usage(cpu_usage, mem_data, bars=20):
    cpu_usage_percentage = cpu_usage / 100
    cpu_bar = "█" * int(cpu_usage_percentage * bars) + "-" * (bars - int(cpu_usage_percentage * bars))

    memory_usage_percentage = mem_data.percent / 100
    memory_bar = "█" * int(memory_usage_percentage * bars) + "-" * (bars - int(memory_usage_percentage * bars))
    available_memory = ((mem_data.available / BYTES_IN_GB) / TOTAL_MEMORY) * 100
    print(f"\r"
          f"{'CPU Usage:'.ljust(LABEL_WIDTH)} |{cpu_bar}| {str(f'{cpu_usage:.2f}%').rjust(6)}  "
          f"{'Memory Usage:'.ljust(LABEL_WIDTH)} |{memory_bar}| {str(f'{memory_usage_percentage *100 :.2f}%').rjust(6)}  "
          f"{'Available Memory:'.ljust(LABEL_WIDTH)} {str(f'{available_memory:.2f}%').rjust(6)}",
          end="")

