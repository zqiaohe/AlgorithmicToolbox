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
            self.Size += 1
            self.Head = element(value)
            self.Head.next = element(value)
            self.Head.next.last = self.Head
            self.Tail = self.Head
        else:
            self.Head.next = element(value)
            self.Head.next.last = self.Head
            self.Head = self.Head.next
            if self.Size < self.Capacity:
                if self.Dict.get(key) is None or self.Tail == self.Dict.get(key):
                    self.Size += 1
                elif self.Dict.get(key) is not None and self.Tail != self.Dict.get(key) :
                    self.Dict.get(key).last.next = self.Dict.get(key).next
                    self.Dict.get(key).next.last = self.Dict.get(key).last
            else:
                if self.Dict.get(key) is None or self.Tail == self.Dict.get(key):
                    self.Tail.value = -1
                    self.Tail = self.Tail.next
                elif self.Dict.get(key) is not None and self.Tail != self.Dict.get(key) :
                    self.Dict.get(key).last.next = self.Dict.get(key).next
                    self.Dict.get(key).next.last = self.Dict.get(key).last

        self.Dict[key] = self.Head


    def get(self, key):
        if self.Dict.get(key) is None:
            return -1
        else:
            print(self.Dict.get(key).value)
            self.put(key, self.Dict.get(key).value)
            print(self.Dict.get(key).value)
            return self.Dict.get(key).value

# cache = LRUCache(5)
#
# cache.put(2, 2)
# cache.put(4, 4)
# cache.put(3, 3)
# cache.put(1, 1)
# cache.put(1, 1)
# cache.put(1, 1)
# cache.put(10, 10)
# cache.put(120, 120)
# cache.put(35, 35)
# print(cache.Size)
# print(cache.Head.value, cache.Tail.value)
# print('mau', cache.Tail.value)

# cache = LRUCache( 2 )
#
# cache.put(1, 1)
# cache.put(2, 2)
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

# cache = LRUCache(2)
# print(cache.get(2))
# cache.put(2, 6)
# print(cache.get(1))
# cache.put(1, 5)
# cache.put(1, 2)
# print(cache.get(1))
# print(cache.get(2))

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))
# cache.put(3, 3)
# print(cache.get(2))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))

# ["LRUCache","put","get","put","get","get"]
# [[1],[2,1],[2],[3,2],[2],[3]]

cache = LRUCache(1)

cache.put(2, 1)
print(cache.get(2))
cache.put(3, 2)
print(cache.get(2))
print(cache.get(3))
print(cache.Tail.value)