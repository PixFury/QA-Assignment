import psutil
from datetime import datetime

CPU_THRESHOLD = 80.0  
MEMORY_THRESHOLD = 80.0  
DISK_THRESHOLD = 90.0  
PROCESS_THRESHOLD = 300  

LOG_FILE = "/var/log/system_health.log"

def log_message(message):
    print(message)
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"ALERT: High CPU usage detected: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"ALERT: High Memory usage detected: {memory_usage}%")

def check_disk():
    disk_usage = psutil.disk_usage("/")
    disk_usage_percent = disk_usage.percent
    if disk_usage_percent > DISK_THRESHOLD:
        log_message(f"ALERT: High Disk usage detected: {disk_usage_percent}%")

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_message(f"ALERT: High number of running processes detected: {process_count}")

def check_system_health():
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

if __name__ == "__main__":
    check_system_health()