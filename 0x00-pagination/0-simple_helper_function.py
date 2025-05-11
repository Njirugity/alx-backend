#!/usr/bin/env python3
"""
return a tuple of size two containing
a start index and an end index
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    takes two integer arguments page
    and page_size
    """

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
