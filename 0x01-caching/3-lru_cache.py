#!/usr/bin/env python3

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add a key-value pair to the cache using LRU algorithm."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in\
               self.keys:
            lru_key = self.keys.pop(0)
            self.cache_data.pop(lru_key)
            print(f"DISCARD: {lru_key}")
        
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
