#!/usr/bin/env python3
'''implementing FIFOCache.'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''implementing fifo caching system.`'''
    def __init__(self):
        """initializing constructor."""
        super().__init__()

    def put(self, key, item):
        """Add a key-value pair to the cache using FIFO algorithm."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

    def get(self, key):
        """Retrieve a value from the cache."""
        if key is None:
            return None

        return self.cache_data.get(key, None)
