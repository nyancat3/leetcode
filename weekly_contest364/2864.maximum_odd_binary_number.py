class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_of_one = 0
        num_of_digits = 0
        for c in s:
            if c == '1':
                num_of_one += 1
            num_of_digits += 1
        ans = ''
        for i in range(num_of_one - 1):
            ans += '1'
        for i in range(num_of_digits - num_of_one):
            ans += '0'
        ans += '1'
        return ans
