#!/usr/bin/env python3
"""
helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple of start index and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
