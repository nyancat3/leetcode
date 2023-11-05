class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ans = set(range(n))
        for i in range(len(edges)):
            ans.discard(edges[i][1])
        return ans.pop() if len(ans) == 1 else -1
