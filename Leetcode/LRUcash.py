class element:
    last = None
    next = None
    value = None
    def __init__(self, Value: int):
        self.value = Value
class LRUCache:
    Head = None
    Tail = element(-1)
    Capacity = 0
    Dict = {}
    Size = 0
    def __init__(self, capacity: int):
        self.Capacity = capacity

    def put(self, key, value):
        if self.Size == 0:
            self.Dict[key] = element(value)
            self.Head = self.Dict.get(key)
            self.Head.last = self.Tail
            self.Tail.next = self.Head
            self.Size += 1
        elif self.Size < self.Capacity:
            if self.Dict.get(key) is None:
                self.Dict[key] = element(value)
                self.Head.next = self.Dict.get(key)
                self.Dict.get(key).last = self.Head
                self.Head = self.Dict.get(key)
            else:
                self.Dict.get(key).last.next = self.Dict.get(key).next
                self.Dict.get(key).next.last = self.Dict.get(key).last
                self.Head = self.Dict.get(key)
        else:
            self.Tail = self.Tail.next



cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.put(1, 1)
cache.put(3, 100)
print(cache.Tail.value)
# print(cache.get(1))       #// returns 1
# cache.put(3, 3)    #// evicts key 2
# print(cache.get(2))      #// returns -1 (not found)
# cache.put(4, 4)    #// evicts key 1
# print(cache.get(1))       #// returns -1 (not found)
# print(cache.get(3) )      #// returns 3
# print(cache.get(4))       #// returns 4

# cache2 = LRUCache(1)
# cache2.put(2, 1)
# print(cache2.get(2))

# cache3 = LRUCache(2)
# print(cache.get(2))
# cache.put(2, 6)
# print(cache.get(1))
# cache.put(1, 5)
# cache.put(1, 2)
# print(cache.get(1))
# print(cache.get(2))
