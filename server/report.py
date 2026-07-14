"""
NetVision Analytics Report
"""

from server.analytics import (
    get_average_cpu,
    get_max_cpu,
    get_min_cpu,
    get_average_memory,
    get_max_memory,
    total_records
)


def show_report():

    print("\n" + "=" * 60)
    print("               NETVISION ANALYTICS REPORT")
    print("=" * 60)

    print(f"\nAverage CPU     : {get_average_cpu()} %")
    print(f"Maximum CPU     : {get_max_cpu()} %")
    print(f"Minimum CPU     : {get_min_cpu()} %")

    print()

    print(f"Average RAM     : {get_average_memory()} %")
    print(f"Maximum RAM     : {get_max_memory()} %")

    print()

    print(f"Records Stored  : {total_records()}")

    print("\n" + "=" * 60)