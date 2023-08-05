#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # defaultdict returns empty list if the key doesn't exist
        for word in strs:
            word_sorted_list = sorted(word) # O(n log n)
            key = ''.join(word_sorted_list)
            anagram_map[key].append(word)   # append the new word to the list of words inside the map
        return anagram_map.values()

# @lc code=end
