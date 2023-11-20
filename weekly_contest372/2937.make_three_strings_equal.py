class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l_s1, l_s2, l_s3 = len(s1), len(s2), len(s3)
        min_l = min(l_s1, l_s2, l_s3)
        i = 0
        while i < min_l and s1[i] == s2[i] and s2[i] == s3[i]:
            i += 1
        return -1 if i == 0 else l_s1 + l_s2 + l_s3 - i * 3 # i * 3 is the number of common characters in the beginning of s1, s2, s3
