"""
NetVision Database
"""

import sqlite3

DATABASE = "database/netvision.db"


def initialize_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

            hostname TEXT,

            cpu REAL,

            memory REAL,

            disk REAL,

            battery REAL,

            health INTEGER,

            status TEXT

        )
    """)

    connection.commit()

    connection.close()


def save_metrics(metrics):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO metrics
        (
            hostname,
            cpu,
            memory,
            disk,
            battery,
            health,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            metrics["hostname"],
            metrics["cpu"],
            metrics["memory"],
            metrics["disk"],
            metrics["battery"],
            metrics["health"],
            metrics["status"]
        )
    )

    connection.commit()

    connection.close()