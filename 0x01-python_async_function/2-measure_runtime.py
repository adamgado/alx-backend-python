#!/usr/bin/env python3
"""function with integers arguments measure total execution time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n, return a float."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
