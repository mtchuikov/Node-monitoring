import psutil
import http.client
from datetime import datetime
import platform
from db.controller import cursorSystemRequirements

bytes_to_gigabytes = lambda bytes_: round(bytes_ / pow(1024, 3), 2)

snapshot_time = lambda: datetime.now().utcnow().strftime("%Y-%m-%d %H:%M:%S")

def self_ip() -> str:
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return conn.getresponse().read().decode("utf-8")


def collect_system_requirements():
    for disk_number, disk_part in enumerate(psutil.disk_partitions(all=False), 1):
        disk = psutil.disk_usage(disk_part.mountpoint)
        print(disk)
    cursorSystemRequirements.paste_row(
        {
        "snapshotTime": snapshot_time(),
        "cpuCount": psutil.cpu_count(),
        "cpuFrequency": round(psutil.cpu_freq().current / 1000, 2),
        "totalRam": bytes_to_gigabytes(psutil.virtual_memory().total),
        "totalStorage":" ",
        }
    )
    cursorSystemRequirements.commit()

collect_system_requirements()