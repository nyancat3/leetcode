#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time Complexity: (n - k) * log n = O(nlogn)
        # if the number of elements is more than k, have to pop it n-k times
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # Time O(n) Transform list x into a heap, in-place, in linear time.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # O(log n)

    def add(self, val: int) -> int:
        # Time Complexity: n * log n = O(nlogn) ?
        heapq.heappush(self.minHeap, val)   # O(log n)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(log n)
        return self.minHeap[0]  # O(1)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
