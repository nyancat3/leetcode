#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def search_recursive(curr: Trie, word: str):
            count = 0
            for c in word:
                if c == '.':
                    for child in curr.children.values():
                        print(word[count + 1:])
                        found_path = search_recursive(child, word[count + 1:])
                        if found_path:
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                count += 1
            return curr.end_of_word

        curr = self.root
        return search_recursive(curr, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
