from base_caching import BaseCaching

class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.access_time = {}
        self.current_time = 0

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            items_to_discard = [k for k, v in self.frequency.items() if v == min_frequency]

            if len(items_to_discard) > 1:
                lru_item = min(self.access_time, key=lambda k: self.access_time[k])
                items_to_discard.remove(lru_item)

            for key_to_discard in items_to_discard:
                del self.cache_data[key_to_discard]
                del self.frequency[key_to_discard]
                del self.access_time[key_to_discard]
                print(f"DISCARD: {key_to_discard}")

        self.cache_data[key] = item
        self.access_time[key] = self.current_time
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.current_time += 1

    def get(self, key):
        if key is None:
            return None

        if key in self.cache_data:
            self.access_time[key] = self.current_time
            self.frequency[key] += 1
            self.current_time += 1
            return self.cache_data[key]

        return None
