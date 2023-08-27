class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # O(n) solution
        l_count = moves.count('L')  # Time complexity of str.count: O(n)
        r_count = moves.count('R')  # Time complexity of str.count: O(n)
        u_count = len(moves) - l_count - r_count    # Time complexity of len(): O(1)
        return u_count + abs(l_count - r_count)
