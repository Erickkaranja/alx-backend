#!/usr/bin/env python3
'''implementing most recent used(MRU) caching algorithm.'''

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''initializing class MRUCache.'''
    def __init__(self):
        '''initializing constructors.'''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add a key-value pair to the cache using MRU algorithm."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in\
           self.keys:
            mru_key = self.keys.pop()
            self.cache_data.pop(mru_key)
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Retrieve a value from the cache, updating usage order."""
        if key is None:
            return None

        value = self.cache_data.get(key, None)
        if value is not None:
            self.keys.remove(key)
            self.keys.append(key)

        return value
