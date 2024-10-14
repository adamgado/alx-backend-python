#!/usr/bin/env python3
"""code nearly identical to wait_n except task_wait_random is being called"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delays = [task_wait_random(max_delay) for x in range(n)]
    delays = asyncio.as_completed(delays)
    delay_list = [await a for a in delays]
    return delay_list
