class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = set(range(n))
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    ans.discard(j)
        return ans.pop()
