class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        ans = []

        for i in range(100, 1000, 2):
            d1, d2, d3 = i // 100, (i // 10) % 10, i % 10
            nums = Counter([d1, d2, d3])
            valid = True
            for num, freq in nums.items():
                if count[num] < freq:
                    valid = False
                    break
            if valid:
                ans.append(i)
        return ans
