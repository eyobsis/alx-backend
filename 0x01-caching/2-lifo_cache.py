#!/usr/bin/env python3

'''
This Python module implements a simple Last-In-First-Out (LIFO) caching system,
also known as stack-based caching. It inherits from a base `BaseCaching` class
(not shown here) which likely provides shared functionality for various caching
implementations.
'''

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
   '''
   `LIFOCache` class implements a caching system that evicts the most recently
   used item when the cache reaches its maximum capacity. This is often referred
   to as a stack-based cache due to its LIFO behavior.
   '''

   def __init__(self):
       '''
       Initializer for the `LIFOCache` class.
       - Calls the superclass (`BaseCaching`) initializer.
       - Initializes an `OrderedDict` named `cache_data` to store key-value pairs.
         - `OrderedDict` is used to facilitate LIFO eviction by tracking insertion order.
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
       - Moves the new key to the end of the `OrderedDict` to maintain LIFO order.
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
       '''
       Retrieves a value from the cache associated with the provided key.
       - Uses the `get` method of `OrderedDict` to retrieve the value for the key.
       - Returns `None` if the key is not found.
       - Does not affect the ordering of items in the cache.
       '''

       return self.cache_data.get(key, None)
