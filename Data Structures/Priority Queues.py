# Construction: Heaps: O(n)
# Appending: Heaps: O(log(n))
# Popping/Polling (dequeuing): Heaps: O(log(n))
# Peeking: Heaps: O(1)
# Removing: O(log(n))
# Advanced Removing (with help from hash table): O(log(n))
# Contains: O(n)
# Contains check with help from hash table: O(1) 

import heapq

data = [4, 2, 6, 1, 7, 8, 9, 5]
heapq.heapify(data)

print(data)