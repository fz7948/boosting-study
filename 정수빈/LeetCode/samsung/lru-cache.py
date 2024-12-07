# https://leetcode.com/problems/lru-cache/?envType=company&envId=samsung&favoriteSlug=samsung-three-months
# 난이도: medium
# 설명: 링크드 해시맵에 해당하는 OrderedDict 사욜하면 더 좋은 결과를 냈을듯, collections.OrderedDict(), move_to_end, popitem
# 캐시에서 get, put 구현하는 문제, 캐시에는 크기 제한이 있다. 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.q = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.q.remove(key)
    
        self.q.append(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            while len(self.q) > self.capacity:
                k = self.q.pop(0)
                del self.cache[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)