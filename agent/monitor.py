"""
NetVision Monitor

Collects live system statistics.
"""

import platform
import psutil


def get_system_info():
    """
    Collect current system information.
    """

    battery = psutil.sensors_battery()

    return {
    "hostname": platform.node(),
    "os": platform.system(),
    "cpu": round(psutil.cpu_percent(interval=1), 1),
    "memory": round(psutil.virtual_memory().percent, 1),
    "disk": round(psutil.disk_usage("/").percent, 1),
    "battery": battery.percent if battery else "N/A",
    "username": psutil.Process().username()
}