#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            # pop
        self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
