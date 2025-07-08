A terminal-based system monitor written in Python.  
Displays real-time CPU and memory usage, lists active processes, and allows user interaction for sorting and exiting.

## 📦 Features

- ✅ Live CPU and memory usage bars
- ✅ Sorted list of active processes (by CPU, RAM, or name)
- ✅ Color-coded process usage (red for high CPU, yellow for high RAM)
- ✅ Interactive user input for sorting
- ✅ Clean exit via `exit` or `x` command
- ✅ Threaded architecture for smooth, concurrent updates

## 🖥️ Interface Overview
CPU Usage:       |██████████--------|  52.00%   Memory Usage:    |███████-----------|  35.00%   Available Memory:   65.00%
PID      Name                      CPU %     RAM %
1234     chrome.exe                 78.2      12.5 5678     python.exe                 23.1       8.3 

## 🧠 How It Works

- `display_usage()` updates CPU and memory bars every second
- `display_processes()` refreshes top N processes every 5 seconds
- `listen_for_input()` waits for user input to change sorting or exit
- All components run in separate threads and share a global `running` flag

## 🧪 Usage

### ▶️ Run the program

```bash
python main.py

⌨️ Commands
- 1 → Sort by CPU usage
- 2 → Sort by RAM usage
- 3 → Sort by process name
- exit or x → Exit the program
🛠️ Requirements
- Python 3.6+
- psutil(pip install psutil)

📁 File Structur
.
├── main.py                # Entry point, starts all threads
├── display_functions.py   # Core logic for display and input
└── README.md              # Project documentation

📌 Notes
- Designed for Windows terminal (uses os.system("cls") and ANSI codes)
- For Linux/macOS, replace cls with clear if needed
- Tested in standard terminal environments

👨‍💻 Author
Miljan D.
