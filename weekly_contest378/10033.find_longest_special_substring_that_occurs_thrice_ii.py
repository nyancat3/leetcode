class Solution:
    def maximumLength(self, s: str) -> int:
        prev_character = s[0]
        count = { prev_character: 1} # { alphabet: count, ... } max length is 26
        sub_strs = { prev_character: { 1: 1 } } # { alphabet: {sub_count: count}, ... } max length is 26. e.g. { a: {1: 4, 2: 3, 3: 0}, b: {1: 0} }
        max_count, ans, sub_str_len = 0, 0, 1

        for i in range(1, len(s)):
            character = s[i]
            count[s[i]] = count.get(s[i], 0) + 1
            max_count = max(max_count, count[s[i]])
            if prev_character == character:
                sub_str_len += 1
            else:
                sub_str_len = 1
                prev_character = character

            if character not in sub_strs:
                sub_strs[character] = {}
            sub_strs[character][sub_str_len] = sub_strs.get(character, {}).get(sub_str_len, 0) + 1
            prev_character = character
        if max_count < 3:
            return -1

        for character in sub_strs: # at most 26
            pre_sum = 0
            for j in range(count[character], 0, -1):
                pre_sum += sub_strs[character].get(j, 0)
                if pre_sum >= 3:
                    ans = max(ans, j)
                    break
        return ans
