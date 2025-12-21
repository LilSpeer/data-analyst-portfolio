import psutil

def check_disks():
    disks = []
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disks.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System": partition.fstype,
            "Total Size (GB)": round(usage.total / (1024 ** 3), 2),
            "Used Size (GB)": round(usage.used / (1024 ** 3), 2),
            "Free Size (GB)": round(usage.free / (1024 ** 3), 2),
            "Usage (%)": usage.percent,
        })
        if usage.percent > 85:
            print(f"Warning: High disk usage on {partition.device}, ({usage.percent}%)")
    return disks