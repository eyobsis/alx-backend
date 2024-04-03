#!/usr/bin/env python3

"""
This Python module provides various caching implementations: FIFO,
LIFO, LRU, MRU,
and LFU. It leverages a base `BaseCaching` class (not shown here) 
for potential
shared functionality across different caching strategies.
"""

from collections import OrderedDict


class BaseCaching:
    """
    Base class for various caching implementations (not shown in detail).
    Likely provides shared attributes or methods for caching functionality.
    """

    MAX_ITEMS = 100  # Example maximum number of items in the cache


class FIFOCache(BaseCaching):
    '''
    `FIFOCache` class implements a caching system that evicts the 
    least recently
    inserted item when the cache reaches
    its maximum capacity (First-In-First-Out).
    '''

    def __init__(self):
        '''
        Initializer for the `FIFOCache` class.
        - Calls the superclass (`BaseCaching`) initializer.
        - Initializes an `OrderedDict` named `cache_data` to store
        key-value pairs.
          - `OrderedDict` helps maintain the insertion order
          for FIFO eviction.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        This method adds a key-value pair to the cache.
        - Checks for invalid input (key or item being None).
        - Evicts the least recently used item if the cache is full:
        - Removes the first inserted item (key) using `popitem(last=False)`.
        - Prints a message indicating the discarded key using
        f-string formatting.
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
        - Uses the `get` method of `OrderedDict` to retrieve 
        the value for the key.
        - Returns `None` if the key is not found.
        '''

        return self.cache_data.get(key, None)


class LIFOCache(BaseCaching):
    '''
    `LIFOCache` class implements a caching system that evicts
    the most recently
    inserted item when the cache reaches its maximum capacity (Last-In-First-Out,
    also known as stack-based caching).
    '''

    def __init__(self):
        '''
        Initializer for the `LIFOCache` class.
        - Calls the superclass (`BaseCaching`) initializer.
        - Initializes an `OrderedDict` named `cache_data` 
        to store key-value pairs.
        - `OrderedDict` is used to facilitate 
        LIFO eviction by tracking insertion order.
        '''

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        This method adds a key-value pair to the cache.
        - Checks for invalid input (key or item being None).
        - Discards the most recently used item if the cache is full:
        - Removes the last inserted item (key) using `popitem(True)`.
        - Prints a message indicating the discarded key.
        - Adds the new key-value pair to the `cache_data` dictionary.
        - Moves the new key to the end of the `OrderedDict` to maintain 
        LIFO order.
        '''

        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)  # Ensure LIFO order

        def get(self, key):
        """
         Retrieves a value from the cache associated
         with the provided key.
        - Uses the `get` method of `OrderedDict` to retrieve the value
        for the key.
        - Returns `None` if the key is not found.
        - Does not affect the ordering of items in the cache.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
