# My Competitive-Programming Journey
# Contents

## Data Structures
### Python Data Structure Characteristics

### Overview
### Here is a list of Data Structures that will be covered
Lists
Multi-Dimensional Lists
Arrays
Dictionaries
Sets
Tuples
Linked-Lists
Queues
Stacks
### Priority Queues --> Heaps (optimal priority queues)
Used in Djikstra's Shortest Path and Prim's Minimum Spanning Tree

### Initialization
#### Lists: 
    myList = []
#### Arrays: 
    import array as arr
    myArr = arr.array('i', [1, 2 , 3])
#### Dictionaries: 
    myDict = {} --> Empty dict NOT empty set
#### Sets: 
    mySet = {'a','b','c'} OR mySet = set(['a','b','c'])
#### Tuples: 
    myTuple = (a,b)
#### Linked-Lists: 
    LL = LinkedList()
    LL.head = Node(3)
#### Queues: 
    from queue import Queue
    q = Queue(mazesize = n)
#### Stacks: 
    from queue import LifoQueue
    stack = LifoQueue(mazesize=3)
#### Priority Queues (Heap Queues): 
    import heapq
    myList = [1, 2, 3]
    heapq.heapify(myList) 
 
### Copying
    .copy(x) --> returns a shallow copy of x
    .deepcopy(x) --> returns a deep copy of x

### Mutable
    Lists: Yes
    Dictionaries: Yes
    Tuples: No
    Sets: Yes 
    Frozen Set: No --> frozen() to change to change set to frozen set
    Byte Array: Yes

### Ordered:
    Lists: Yes
    Tuples: Yes
    Sets: No

### Indexing/Slicing:
    Lists: Yes
    Tuples: Yes
    Sets: No

# Duplicate Elements:
    Lists: Yes
    Tuples: Yes
    Sets: No

## Python Time Complexity (Big O Notation)

### Order
    O(1) --> Amazing
    O(logN) --> Great
    O(N) --> Good
    O(N+k) --> Good 
    O(N logN) --> Bad
    O((N logN)^2) --> Really Bad
    O(2^n) --> Horrible
    O(n!) --> Atrocious

### Appending
    Lists: O(1)
    Dicts: O(1)
    Sets: O(1)

### Indexing
    Lists: O(1)
    Dictionaries: O(1)
    Sets: O(1)

### If Val in Data Structure
    Lists: O(N)
    Dictionaries: O(1)
    Sets: O(1)

### For val in Data Structure
    Lists: O(N)
    Dictionaries: O(N)
    Sets: O(N)

### Sorting (.sort()):
    Lists: O(N logN)


## Algorithms
Breadths First Search, Depth First Search, Djikstra's Shortest, Dynamic Programming, Recursion


