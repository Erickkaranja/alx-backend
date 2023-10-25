#!/usr/bin/env python3
'''creating a basic cache module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''creates a basic cache system.'''
    def put(self, key, item):
        '''adds a key value pair into the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''retrieves value from the cache.'''
        if key is not None:
            return self.cache_data.get(key, None)
        return None
