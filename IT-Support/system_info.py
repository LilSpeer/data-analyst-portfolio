import psutil
import platform
from gpu_info import get_gpu_info
def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "Used RAM (%)": psutil.virtual_memory().percent,
        "GPU(s)": get_gpu_info()
    }
