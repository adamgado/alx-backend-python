#!/usr/bin/env python3
"""function takes string and number arguments and returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of string and square of a number"""
    return (k, v ** 2)
