#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        dict = {} # key: char, value: array index
        head = tail = 0
        while head < len(s) and tail < len(s): # O(n). head < len(s) condition can be deleted cuz the last run of tail returns the longest length for the tail.
            tail_letter = s[tail]
            if tail_letter in dict: # O(1) cos using hash table
                head = max(head, dict[tail_letter] + 1) # If head is bigger than dictionary's value, set head index cuz head cannot go back
            dict[tail_letter] = tail
            ans = max(ans, tail - head + 1)
            tail += 1
        return ans

        # Brute force: O(n^3)
        def check(start, end):
            chars = [0] * 128 # Alphanumeric is consisted by 128 codes
            for c in s[start:end + 1]:
                if chars[ord(c)] == 1: # Convert char into Unicode
                    return False
                else:
                    chars[ord(c)] += 1
            return True

        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j):
                    ans = max(ans, j - i + 1)
        return ans
# @lc code=end
