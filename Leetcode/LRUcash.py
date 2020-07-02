# class queue():
#     class element:
#         last = None
#         next = None
#         value = None
#         __init__(self, Value: int):
#             self.value = Value
#     Queue = []
#     head = None
#     tail = None
#     Capacity = 0
#     def __init__(self, capacity: int):
#         self.Capacity = capacity

class LRUCache:
    Dict = {}
    Queue = queue()
    Capacity = 0
    def __init__(self, capacity: int):
        self.Capacity = capacity

    def get(self, key: int) -> int:
        self.Headindex = len(self.Queue)
        print(type(self.Dict.get(key)))
        if self.Dict.get(key) is not None and self.Dict.get(key) > (len(self.Queue) - self.Capacity - 1) :
            Value = self.Queue[self.Dict.get(key)]
            self.put(key, Value)
            return Value
        else:
            return -1

    def put(self, key: int, value: int):
        self.Queue.append(value)
        self.Dict[key] = len(self.Queue)-1

# cache = LRUCache(2)
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

# cache3 = LRUCache(2)
# print(cache.get(2))
# cache.put(2, 6)
# print(cache.get(1))
# cache.put(1, 5)
# cache.put(1, 2)
# print(cache.get(1))
# print(cache.get(2))