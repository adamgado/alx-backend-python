#!/usr/bin/env python3
"""function takes a float argument and returns multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(float):
        return multiplier * float
    return multiply
