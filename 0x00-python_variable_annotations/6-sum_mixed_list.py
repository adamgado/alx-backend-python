#!/usr/bin/env python3
"""function takes a list of numbers and returns their sum as float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of numbers in a list"""
    return sum(mxd_lst)
