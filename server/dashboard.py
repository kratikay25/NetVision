"""
Professional NetVision Dashboard
"""

import os


def clear_screen():
    os.system("clear")


def show_dashboard(agent_manager):

    clear_screen()

    print("=" * 90)
    print("                         NETVISION LIVE DASHBOARD")
    print("=" * 90)

    print(f"\nConnected Agents : {agent_manager.count()}\n")

    agents = agent_manager.get_all()

    if not agents:
        print("No connected agents.")
        return

    print("+----------------------------+----------+-------+-------+-------+----------+")

    print("| Hostname                   | Status   | CPU   | RAM   | Disk  | Battery |")

    print("+----------------------------+----------+-------+-------+-------+----------+")

    for hostname, info in agents.items():

        print(
            f"| "
            f"{hostname[:26]:<26} | "
            f"{info['status']:<8} | "
            f"{str(info['cpu'])+'%':<5} | "
            f"{str(info['memory'])+'%':<5} | "
            f"{str(info['disk'])+'%':<5} | "
            f"{str(info['battery'])+'%':<8} |"
        )

    print("+----------------------------+----------+-------+-------+-------+----------+")

    print("\n" + "=" * 90)