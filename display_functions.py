
def display_usage(cpu_usage, mem_usage, bars=30):
    cpu_usage_percentage = cpu_usage / 100
    cpu_bar = "█" * int(cpu_usage_percentage * bars) + "-" * (bars - int(cpu_usage_percentage * bars))

    memory_usage_percentage = mem_usage / 100
    memory_bar = "█" * int(memory_usage_percentage * bars) + "-" * (bars - int(memory_usage_percentage * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  "
          f"Memory Usage: |{memory_bar}| {mem_usage:.2f}%  ", end="")
