#!/usr/bin/env python3
"""async routine called that takes in 2 int arguments"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delays = [wait_random(max_delay) for x in range(n)]
    delays = asyncio.as_completed(delays)
    delay_list = [await a for a in delays]
    return delay_list
