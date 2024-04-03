#!/usr/bin/env python3

'''
This Python module implements a Least Recently Used (LRU) caching system.
It inherits from a base `BaseCaching` class (not shown here) which likely provides
shared functionality for various caching implementations.
'''

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
   '''
   `LRUCache` class implements a caching system that evicts the least recently used
   item when the cache reaches its maximum capacity. It prioritizes keeping items
   that have been accessed more recently.
   '''

   def __init__(self):
       '''
       Initializer for the `LRUCache` class.
       - Calls the superclass (`BaseCaching`) initializer.
       - Initializes an `OrderedDict` named `cache_data` to store key-value pairs.
         - `OrderedDict` helps maintain access order for identifying the LRU item.
       '''

       super().__init__()
       self.cache_data = OrderedDict()

   def put(self, key, item):
       '''
       This method adds a key-value pair to the cache.
       - Checks for invalid input (key or item being None).
       - Discards the least recently used item if the cache is full:
           - Removes the least recently accessed key using `popitem(True)`.
           - Prints a message indicating the discarded key.
       - Adds the new key-value pair to the cache.
       - Moves the newly added key to the front of the `OrderedDict` to mark it as recently used.
       '''

       if key is None or item is None:
           return

       if key not in self.cache_data:
           if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
               lru_key, _ = self.cache_data.popitem(True)  # Remove LRU item
               print("DISCARD:", lru_key)

       self.cache_data[key] = item
       self.cache_data.move_to_end(key, last=False)  # Mark as recently used

   def get(self, key):
       '''
       Retrieves a value from the cache associated with the provided key.
       - If the key is found, moves it to the front of the `OrderedDict` to
         mark it as recently used.
       - Returns the value for the key, or `None` if the key is not found.
       '''

       if key is not None and key in self.cache_data:
           self.cache_data.move_to_end(key, last=False)  # Update access order
       return self.cache_data.get(key, None)
