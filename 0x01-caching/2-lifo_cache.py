#!/usr/bin/env python3
'''implementing the lifo caching system.'''
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
'''initializing class LIFOCache'''
    def __init__(self):
        '''initializing constructor.'''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add a key-value pair to the cache using LIFO algorithm."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in\
               self.keys:
            last_key = self.keys.pop()
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")
       
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Retrieve a value from the cache."""
        if key is None:
            return None

        return self.cache_data.get(key, None)
