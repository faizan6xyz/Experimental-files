import psutil, time, os  
# CPU Usage
# Definition: Returns current CPU usage percentage
# Function: Shows how much CPU is being used right now
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

# CPU Core Count
# Definition: Returns number of CPU cores
# Function: Helps understand processing power
print("CPU Cores:", psutil.cpu_count())

# RAM Info
# Definition: Returns memory statistics
# Function: Gives total, used, and available RAM
ram = psutil.virtual_memory()
print("Total RAM:", round(ram.total / (1024**3), 2), "GB")
print("Used RAM:", round(ram.used / (1024**3), 2), "GB")
print("RAM Usage:", ram.percent, "%")

# Disk Usage
# Definition: Returns disk usage stats
# Function: Shows how much storage is used
disk = psutil.disk_usage('/')
print("Disk Usage:", disk.percent, "%")

# Battery Info
# Definition: Gets battery details (if available)
# Function: Shows battery percentage
battery = psutil.sensors_battery()
if battery:
    print("Battery:", battery.percent, "%")

# Boot Time
# Definition: Returns system start time
# Function: Used to calculate uptime
print("System Boot Time:", psutil.boot_time())

# CPU per core usage
print("Per Core Usage:", psutil.cpu_percent(percpu=True))

# Physical vs Logical cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Logical cores:", psutil.cpu_count(logical=True))

# CPU frequency
# Definition: Current CPU speed
print("CPU freq:", psutil.cpu_freq())

# RAM detailed info
ram = psutil.virtual_memory()
print("Total:", ram.total)
print("Available:", ram.available)
print("Used:", ram.used)
print("Free:", ram.free)
print("Percent:", ram.percent)

# Disk partitions
# Definition: Returns all disk drives
# Function: Shows mounted drives and file systems
partitions = psutil.disk_partitions()
for p in partitions:
    print("Device:", p.device)
    print("Mountpoint:", p.mountpoint)
    print("File system:", p.fstype)

    usage = psutil.disk_usage(p.mountpoint)
    print("Usage:", usage.percent, "%")
    print("-" * 20)

# Network usage
# Definition: Returns network stats
# Function: Shows data sent/received
net = psutil.net_io_counters()
print("Bytes Sent:", net.bytes_sent)
print("Bytes Received:", net.bytes_recv)

# Uptime
boot = psutil.boot_time()
uptime = time.time() - boot
print("Uptime (seconds):", uptime)

# Process list
# Definition: Lists running processes
# Function: Shows PID, name, CPU usage
for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    print(process.info)

# Current process info
p = psutil.Process(os.getpid())
print("Process name:", p.name())
print("CPU usage:", p.cpu_percent())
print("Memory:", p.memory_info())

# Battery detailed
battery = psutil.sensors_battery()
if battery:
    print("Percent:", battery.percent)
    print("Plugged in:", battery.power_plugged)

# Top CPU processes
processes = []
for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    processes.append(p.info)

processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
for p in processes[:5]:
    print(p)

# Load average
# Definition: System load over time
print("Load Average:", psutil.getloadavg())

# CPU time distribution
cpu_times = psutil.cpu_times()
print(cpu_times)

# Swap memory
swap = psutil.swap_memory()
print("Swap Total:", swap.total)
print("Swap Used:", swap.used)
print("Swap Percent:", swap.percent)

# Disk I/O
disk_io = psutil.disk_io_counters()
print("Read bytes:", disk_io.read_bytes)
print("Write bytes:", disk_io.write_bytes)

# Network speed
old = psutil.net_io_counters()
time.sleep(1)
new = psutil.net_io_counters()
print("Upload speed:", new.bytes_sent - old.bytes_sent, "bytes/sec")
print("Download speed:", new.bytes_recv - old.bytes_recv, "bytes/sec")

# Memory usage per process
for p in psutil.process_iter(['pid', 'name', 'memory_percent']):
    print(p.info)

# High CPU processes
for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    if p.info['cpu_percent'] > 10:
        print(p.info)

# Open files
p = psutil.Process()
print(p.open_files())

# Logged-in users
users = psutil.users()
for user in users:
    print(user.name, user.host)

# Boot time readable
boot = psutil.boot_time()
print("Boot Time:", time.ctime(boot))

# Threads
p = psutil.Process()
print("Threads:", p.num_threads())
print("Thread details:", p.threads())

# Network connections of process
p = psutil.Process()
print(p.net_connections())

# Child processes
p = psutil.Process()
print(p.children(recursive=True))

# CPU affinity
# Definition: Assign process to specific CPU core
p.cpu_affinity([0])
print(p.cpu_affinity())

# Memory maps
p = psutil.Process()
print(p.memory_maps())

# Context switches
p = psutil.Process()
print(p.num_ctx_switches())

# Handles (Windows)
p = psutil.Process()
print(p.num_handles())

# All system connections
for conn in psutil.net_connections():
    print(conn)

# Disk partitions (again summary)
for part in psutil.disk_partitions():
    print(part)

# Virtual memory full object
vm = psutil.virtual_memory()
print(vm)

# System summary
print("CPU:", psutil.cpu_percent(), "%")
print("RAM:", psutil.virtual_memory().percent, "%")
print("Swap:", psutil.swap_memory().percent, "%")
print("Processes:", len(psutil.pids()))

# Zombie processes
for p in psutil.process_iter(['pid', 'name', 'status']):
    if p.info['status'] == 'zombie':
        print("Zombie process:", p.info)

# Live monitor loop
# Definition: Continuous monitoring
# Function: Shows real-time CPU & RAM usage
while True:
    print("CPU:", psutil.cpu_percent(), "%")
    print("RAM:", psutil.virtual_memory().percent, "%")
    print("-" * 30)
    time.sleep(1)