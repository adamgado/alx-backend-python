#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random delay and eventually returns it"""
    rand_delay = random.random() * max_delay
    await asyncio.sleep(rand_delay)
    return rand_delay
