class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = ''
        for char in order:
            if char in counter:
                ans += char * counter.pop(char)
        for char, num in counter.items():
            ans += char * num
        return ans
