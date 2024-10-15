#!/usr/bin/env python3
"""coroutine that will execute async_comprehension four times in parallel"""
import asyncio
import random
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for a in range(4)))
    return time.time() - start
