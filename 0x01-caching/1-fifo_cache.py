#!/usr/bin/env python3
"""A script for FIFO caching system
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = next(iter(self.cache_data))
            self.cache_data.pop(del_key)
            print(f"DISCARD: {del_key}")

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None."""
        data = self.cache_data
        if key is not None and key in data:
            return self.cache_data[key]
