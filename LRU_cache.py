class Node:
    def __init__(self,key,value):
        self.key, self.val = key,value
        self.prev,self.next = None, None

class LRUcache:
    
    def __init__(self,capacity:int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev =   nxt,prev

    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev,node.next = prev,nxt

    def get(self,key):
        for key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        return self.cache[key].val

    def put(self,key,value):
        for key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Example usage
cache = LRUcache(2)  # Initialize LRU cache with capacity 2
cache.put(1, 1)      # Cache is {1=1}
cache.put(2, 2)      # Cache is {1=1, 2=2}
print(cache.get(1))  # Returns 1, Cache is {2=2, 1=1}
cache.put(3, 3)      # Evicts key 2, Cache is {1=1, 3=3}
print(cache.get(2))  # Returns -1 (not found)
cache.put(4, 4)      # Evicts key 1, Cache is {3=3, 4=4}
print(cache.get(1))  # Returns -1 (not found)
print(cache.get(3))  # Returns 3
print(cache.get(4))  # Returns 4