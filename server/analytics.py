
"""
NetVision Analytics Engine
"""

import sqlite3

DATABASE = "database/netvision.db"


def get_average_cpu():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ROUND(AVG(cpu),2) FROM metrics"
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result


def get_average_memory():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ROUND(AVG(memory),2) FROM metrics"
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result


def total_records():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM metrics"
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result

def get_max_cpu():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ROUND(MAX(cpu),2) FROM metrics"
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result


def get_min_cpu():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ROUND(MIN(cpu),2) FROM metrics"
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result


def get_max_memory():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ROUND(MAX(memory),2) FROM metrics"
    )

    result = cursor.fetchone()[0]

    connection.close()

    return result