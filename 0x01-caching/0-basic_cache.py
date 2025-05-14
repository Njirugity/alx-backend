#!/usr/bin/env python3
"""A script for caching system
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching
    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """initialize BasicCache"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value for the key key
        """
        if key is None and item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key

        Args:
            key (_type_): _description_
        """
        data = self.cache_data
        if key is not None and key in data:
            return self.cache_data[key]
        else:
            return None
