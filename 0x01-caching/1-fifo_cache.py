#!/usr/bin/env python3

'''
This Python module implements a simple First-In-First-Out (FIFO) caching system.
It inherits from a base `BaseCaching` class (not shown here) which likely provides
shared functionality for various caching implementations.
'''

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    `FIFOCache` class implements a caching system that evicts the least recently
    used item when the cache reaches its maximum capacity.
    '''

    def __init__(self):
        '''
        Initializer for the `FIFOCache` class.
        - Calls the superclass (`BaseCaching`) initializer.
        - Initializes an `OrderedDict` named `cache_data` to store key-value pairs.
          - `OrderedDict` helps maintain the insertion order for FIFO eviction.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        This method adds a key-value pair to the cache.
        - Checks for invalid input (key or item being None).
        - Evicts the least recently used item if the cache is full:
            - Removes the first inserted item (key) using `popitem(last=False)`.
            - Prints a message indicating the discarded key using f-string formatting.
        - Adds the new key-value pair to the `cache_data` dictionary.
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''
        Retrieves a value from the cache associated with the provided key.
        - Uses the `get` method of `OrderedDict` to retrieve the value for the key.
        - Returns `None` if the key is not found.
        '''

        return self.cache_data.get(key, None)
