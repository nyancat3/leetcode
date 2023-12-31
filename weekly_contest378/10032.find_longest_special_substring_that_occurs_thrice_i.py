class Solution:
    def maximumLength(self, s: str) -> int:
        dict = {}   # { alphabet: index, ... } max length is 26
        count = {}   # { alphabet: count, ... } max length is 26

        max_count = 0
        for i in range(len(s)):
            array = dict.get(s[i], [])
            array.append(i)
            dict[s[i]] = array
            count[s[i]] = count.get(s[i], 0) + 1
            max_count = max(max_count, count[s[i]])
        if max_count < 3:
            return -1

        print(count)
        print(dict)
        ans = 1
        for alp in dict:
            if len(dict[alp]) < 3:
                continue
            print(len(dict[alp]) - 2)
            for f in range(1, len(dict[alp]) - 2): # len 2 to len(alp) - 2. use slow and fast pointers
                s, sub_count = 0, 0
                while f < len(dict[alp]):
                    print("s: {}, f: {}".format(s, f))
                    if dict[alp][s] + (f - s) == dict[alp][f]:
                        sub_count += 1
                    s += 1
                    f += 1
                print("sub_count: {}".format(sub_count))
                if sub_count >= 3:
                    ans = max(ans, f - s + 1)
                else:
                    break # break out of the inner loop
        return ans
