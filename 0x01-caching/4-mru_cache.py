#!/usr/bin/env python3
"""A script for MRU caching system"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU cache system"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ put key value pair into cache"""
        if key is None and item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {del_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None."""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
