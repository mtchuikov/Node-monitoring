import psutil
import http.client
from datetime import datetime

bytes_to_gigabytes = lambda bytes_: round(bytes_ / pow(1024, 3), 2)

snapshot_time = lambda: {"snapshotTime": datetime.now().utcnow().strftime("%Y-%m-%d %H-%M-%S")}

def self_ip() -> str:
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return conn.getresponse().read().decode("utf-8")

def cpu() -> dict:
    return {
        "cpuCount": psutil.cpu_count(),
        "cpuFrequency": round(psutil.cpu_freq().current / 1000, 2),
        # "usedCpuPercent": round(psutil.getloadavg()[0] / psutil.cpu_count() * 100, 1),
    }

def ram() -> dict:
    ram = psutil.virtual_memory()
    return {
        "totalRam": bytes_to_gigabytes(ram.total),
        "availableRam": bytes_to_gigabytes(ram.available),
        "usedRam":  bytes_to_gigabytes(ram.used),
        "usedRamPercent":  ram.percent,
    }

def storage() -> dict:
    data = {}
    for disk_number, disk_part in enumerate(psutil.disk_partitions(all=False), 1):
        disk = psutil.disk_usage(disk_part.mountpoint)
        data[f"Disk {disk_number}"] = {
            "totalStorage": bytes_to_gigabytes(disk.total),
            "availableStorage": bytes_to_gigabytes(disk.free),
            "usedStorage": bytes_to_gigabytes(disk.used),
            "usedStoragePercent": disk.percent,
        }
    return data

def collect_system_requirements():
    pass

collect_system_requirements()