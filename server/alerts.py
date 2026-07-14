"""
NetVision Alert Engine
"""


def check_alerts(agent):

    alerts = []

    if agent["cpu"] > 85:
        alerts.append("HIGH CPU USAGE")

    if agent["memory"] > 85:
        alerts.append("HIGH MEMORY USAGE")

    if agent["disk"] > 90:
        alerts.append("LOW DISK SPACE")

    battery = agent["battery"]

    if isinstance(battery, (int, float)):

        if battery < 20:
            alerts.append("LOW BATTERY")

    return alerts