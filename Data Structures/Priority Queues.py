# Construction
    # Heaps: O(n)

# Appending
    # Heaps: O(log(n))

# Popping/Polling (dequeuing)
    # Heaps: O(log(n))

# Peeking
    # Heaps: O(1)

import heapq

data = [4, 2, 6, 1, 7, 8, 9, 5]
heapq.heapify(data)

print(data)