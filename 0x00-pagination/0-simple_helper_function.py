#!/usr/bin/env python3
"""Write a function named index range"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    start index and an end the page
    """
    return ((page-1) * page_size, page_size * page)
