class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l_s1, l_s2, l_s3 = len(s1), len(s2), len(s3)
        min_l = min(l_s1, l_s2, l_s3)

        if s1[0] != s2[0] or s2[0] != s3[0]:
            return -1

        ans  = l_s1 + l_s2 + l_s3 - min_l * 3
        same_count = 0
        for i in range(min_l):
            if s1[i] != s2[i] or s2[i] != s3[i]:
                break
            same_count += 1

        ans += min_l * 3 - same_count * 3

        return ans
