"""
NetVision Enterprise Dashboard
"""

import os
from datetime import datetime


def clear_screen():
    os.system("clear")


def show_dashboard(agent_manager):

    clear_screen()

    print("=" * 110)
    print("                         NETVISION ENTERPRISE DASHBOARD")
    print("=" * 110)

    print(f"\nConnected Agents : {agent_manager.count()}")
    print(f"Last Refresh     : {datetime.now().strftime('%H:%M:%S')}\n")

    agents = agent_manager.get_all()

    if not agents:
        print("No connected agents.")
        return

    print("+----------------------------+----------+----------+---------+----------+-------+-------+--------+")
    print("| Hostname                   | Status   | LastSeen | OS      | User     | CPU   | RAM   | Health |")
    print("+----------------------------+----------+----------+---------+----------+-------+-------+--------+")

    for hostname, info in agents.items():

        last_seen = info.get("last_seen")

        if last_seen:
            last_seen = last_seen.strftime("%H:%M:%S")
        else:
            last_seen = "--:--:--"

        print(
            f"| "
            f"{hostname[:26]:<26} | "
            f"{info['status']:<8} | "
            f"{last_seen:<8} | "
            f"{info.get('os', '')[:7]:<7} | "
            f"{info.get('username', '')[:8]:<8} | "
            f"{str(info['cpu']) + '%':<5} | "
            f"{str(info['memory']) + '%':<5} | "
            f"{str(info.get('health', 100)):<6} |"
        )

    print("+----------------------------+----------+----------+---------+----------+-------+-------+--------+")
    print("\n" + "=" * 110)