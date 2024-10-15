#!/usr/bin/python3
"""coroutine called async_comprehension that takes no arguments"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return the 10 random numbers"""
    return [a async for a in async_generator()]
