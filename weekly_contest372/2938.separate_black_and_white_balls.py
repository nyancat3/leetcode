class Solution:
    def minimumSteps(self, s: str) -> int:
        zero_count = s.count('0')
        one_count = s.count('1')

        if '0' * zero_count + '1' * one_count == s:
            return 0
        elif len(s) == 1:
            return 0

        ans = 0
        char_list = list(s)
        zero_found = 1 if char_list[0] == '0' else 0

        for i in range(1, len(s)):
            if char_list[i] == '0' and char_list[i - 1] == '1':
                char_list[i - 1] = '0'
                char_list[i] = '1'

                ans += (i - zero_found)
                zero_found += 1
            elif char_list[i] == '0':
                zero_found += 1

        return ans
