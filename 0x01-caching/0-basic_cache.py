#!/usr/bin/env python3
"""Create a class BasicCache task
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """_summary task_
    """

    def __init__(self):
        """_summary task_
        """
        super().__init__()

    def put(self, key, item):
        """_summary task
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value task
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
