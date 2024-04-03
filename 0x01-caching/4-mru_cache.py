#!/usr/bin/env python3

"""
This Python module implements a Most Recently Used (MRU) caching system.
It inherits from a base `BaseCaching` class (not shown here) which likely provides
shared functionality for various caching implementations.

**Note:** MRU cache replacement is not a typical strategy as it prioritizes
keeping the most recently used items, potentially leading to frequently accessed
but less relevant data staying in the cache longer. It might be useful in specific
scenarios where the most recent data is always the most important.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    `MRUCache` class implements a caching system that keeps the most recently used
    items in the cache when it reaches its maximum capacity. This might not be
    the most efficient strategy for most use cases, but it can be useful in specific
    situations where the most recent data is critical.
    '''

    def __init__(self):
        '''
        Initializer for the `MRUCache` class.
        - Calls the superclass (`BaseCaching`) initializer.
        - Initializes an `OrderedDict` named `cache_data` to store key-value pairs.
          - `OrderedDict` helps maintain insertion order, but it's not strictly
            necessary for MRU behavior as all accesses move items to the front.
        '''

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        This method adds a key-value pair to the cache.
        - Checks for invalid input (key or item being None).
        - Discards the least recently used item (which becomes the first in
          `OrderedDict`) if the cache is full:
            - Removes the least recently used item (key) using `popitem(False)`.
            - Prints a message indicating the discarded key.
        - Adds the new key-value pair to the cache.
        - Moves the newly added key to the front of the `OrderedDict` to mark it as MRU
          (though not strictly necessary for MRU behavior as all accesses update order).
        '''

        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(False)  # Remove least recently used
                print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)  # Move to front (not strictly required)

    def get(self, key):
        '''
        Retrieves a value from the cache associated with the provided key.
        - If the key is found, moves it to the front of the `OrderedDict` to
          mark it as recently used (updating MRU order).
        - Returns the value for the key, or `None` if the key is not found.
        '''

        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)  # Update MRU order
        return self.cache_data.get(key, None)
