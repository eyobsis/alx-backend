Project Overview

This project focuses on teaching you about different caching algorithms. By the end, you should be able to explain:

What caching systems are and their purpose
Common caching replacement policies (FIFO, LIFO, LRU, MRU, LFU)
Limitations of caching systems
Requirements

The project requires writing Python code for various caching algorithms. The code must adhere to specific style and formatting guidelines.

Tasks

The tasks involve creating several classes that inherit from a base class BaseCaching. Each class implements a specific caching algorithm:

BasicCache: This is a basic cache with no limit on the number of items it can store.
FIFOCache: This implements the First-In-First-Out (FIFO) algorithm, where the oldest item is discarded when the cache reaches its maximum capacity.
LIFOCache: This implements the Last-In-First-Out (LIFO) algorithm, where the most recently added item is discarded when the cache reaches its maximum capacity.
LRUCache: This implements the Least Recently Used (LRU) algorithm, where the least recently used item is discarded when the cache reaches its maximum capacity.
MRUCache (advanced): This implements the Most Recently Used (MRU) algorithm, where the most recently used item is kept in the cache, and the least recently used is discarded when the cache reaches its maximum capacity.
LFUCache (advanced): This implements the Least Frequently Used (LFU) algorithm, where the item with the lowest frequency of access is discarded when the cache reaches its maximum capacity. If there's a tie for least frequent access, it falls back to LRU for tie-breaking.
Each class should have methods for adding (put) and retrieving (get) items from the cache. The put method should also handle discarding items when the cache is full, printing a message indicating which item was discarded.
