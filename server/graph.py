
"""
NetVision Graph Generator
"""

import sqlite3
import matplotlib.pyplot as plt

DATABASE = "database/netvision.db"


def create_graph(column, title, filename, ylabel):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        f"SELECT timestamp, {column} FROM metrics"
    )

    data = cursor.fetchall()

    connection.close()

    if not data:
        print(f"No data available for {title}.")
        return

    times = [row[0][11:19] for row in data]
    values = [row[1] for row in data]

    plt.figure(figsize=(10, 5))

    plt.plot(times, values, marker="o")

    plt.title(title)

    plt.xlabel("Time")

    plt.ylabel(ylabel)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(f"reports/{filename}")

    plt.close()

    print(f"{filename} generated successfully.")

def generate_all_graphs():

    create_graph(
        "cpu",
        "CPU Usage Over Time",
        "cpu_graph.png",
        "CPU (%)"
    )

    create_graph(
        "memory",
        "Memory Usage Over Time",
        "memory_graph.png",
        "Memory (%)"
    )

    create_graph(
        "disk",
        "Disk Usage Over Time",
        "disk_graph.png",
        "Disk (%)"
    )

    create_graph(
        "battery",
        "Battery Level Over Time",
        "battery_graph.png",
        "Battery (%)"
    )

    create_graph(
        "health",
        "Health Score Over Time",
        "health_graph.png",
        "Health Score"
    )

    print("\nAll graphs generated successfully!")