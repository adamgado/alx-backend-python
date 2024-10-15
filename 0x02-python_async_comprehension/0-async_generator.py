#!/usr/bin/python3
"""coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times, yield a number between 0 and 10"""
    for a in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
