#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time Complexity O(n log n)?
        minusStones = [-s for s in stones]  # list comprehensions https://www.w3schools.com/python/python_lists_comprehension.asp
        heapq.heapify(minusStones)  # O(n)

        while minusStones:
            if len(minusStones) <= 1:
                return -1 * minusStones[0]  # O(1)

            y = heapq.heappop(minusStones)  # O(log n)
            x = heapq.heappop(minusStones)  # O(log n)
            if x != y:
                heapq.heappush(minusStones, y - x)  # O(log n)
        return 0
# @lc code=end
