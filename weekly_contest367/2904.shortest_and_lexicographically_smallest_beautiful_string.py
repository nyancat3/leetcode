class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = "zzzzz"
        beautiful_len = len(s)
        l, r = 0, 0
        count = 0

        while l < len(s) - 1 and s[l] == "0":
            l += 1
        r = l
        # print("test1", l, r)
        while l <= r <= len(s) - 1:
            if s[r] == "1":
                count += 1
            if count == k:
                if (r - l + 1) < beautiful_len:
                    beautiful_len = r - l + 1
                    ans = s[l:r + 1]
                    # print("beautiful_len", beautiful_len, "ans", ans, "s[l:r + 1]", s[l:r + 1])
                elif (r - l + 1) == beautiful_len:
                    ans = min(ans, s[l:r + 1])
                    # print("ans", ans, "s[l:r + 1]", s[l:r + 1])

                # l is always 1
                l += 1
                count -= 1
                while l < len(s) - 1 and s[l] == "0":
                    l += 1
            # print("test2", l, r, count)
            r += 1

        if ans == "zzzzz":
            ans = ""
        return ans
