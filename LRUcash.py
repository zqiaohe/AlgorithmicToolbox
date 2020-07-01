# структура, которая хранит значение, и ссылку на следующее значение и предыдущее
class element:
    Last = None
    Next = None
    Value = None

    def __init__(self, value):
        self.Value = value


class queue():
    head = element(-1)
    Queue = []
    headindex = 0
    Capacity = 0

    def __init__(self, capacity: int):
        self.Capacity = capacity

    def Headindex(self):
        return self.headindex

    def put_element(self, element):
        if len(self.Queue) == 0:
            element.Last = self.head
            self.head.Next = element
            self.head = element
            self.Queue.append(element)
        elif len(self.Queue) < self.Capacity:
            element.Last = self.head
            self.head.Next = element
            self.head = element
            self.Queue.append(element)
            self.headindex += 1
        else:
            element.Last = self.head
            self.head.Next = element
            self.head = element
            self.Queue.append(element)
            self.headindex += 1
            self.Queue[self.headindex - self.Capacity].Value = -1


class LRUCache:
    MyDict = {}
    MyQueue = queue(0)

    def __init__(self, capacity: int):
        self.MyQueue = queue(capacity)

    def get(self, key: int) -> int:
        if self.MyDict.get(key) is None:
            return -1
        else:
            if self.MyDict.get(key).Value == -1:
                return -1
            else:
                self.put(key, self.MyDict.get(key).Value)
                return self.MyDict.get(key).Value

    def put(self, key: int, value: int):
        self.MyQueue.put_element(element(value))
        self.MyDict[key] = self.MyQueue.Queue[self.MyQueue.Headindex()]


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # // returns 1
cache.put(3, 3)  # // evicts key 2
print(cache.get(2))  # // returns -1 (not found)
cache.put(4, 4)  # // evicts key 1
print(cache.get(1))  # // returns -1 (not found)
print(cache.get(3))  # // returns 3
print(cache.get(4))
