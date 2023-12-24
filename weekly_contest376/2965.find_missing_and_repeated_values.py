class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ans = [0, 0]
        num_set = set()
        for i in range(1, n ** 2 + 1):
            num_set.add(i)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in num_set:
                  num_set.remove(grid[i][j])
                else:
                  ans[0] = grid[i][j]
        ans[1] = num_set.pop()
        return ans
