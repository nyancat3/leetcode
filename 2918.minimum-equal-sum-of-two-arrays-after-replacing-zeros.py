class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # c1, c2 = Counter(nums1), Counter(nums2)
        # zero1, zero2 = c1[0], c2[0]
        # sum1, sum2 = sum(nums1), sum(nums2)

        zero1, zero2, sum1, sum2 = 0, 0, 0, 0
        for n in nums1:
            if n == 0:
                zero1 += 1
            sum1 += n
        for n in nums2:
            if n == 0:
                zero2 += 1
            sum2 += n

        diff = abs(sum1 - sum2)

        if sum1 > sum2:
            if zero2 == 0:
                return -1
            elif zero1 == 0 and zero2 > diff:
                return -1
            return max(sum1 + zero1, sum2+  zero2)
        elif sum2 > sum1:
            if zero1 == 0:
                return -1
            elif zero2 == 0 and zero1 > diff:
                return -1
            return max(sum1 + zero1, sum2+  zero2)
        else:
            if zero1 == 0 and zero2 == 0:
                return sum1
            elif zero1 > 0 and zero2 > 0:
                return sum1 + max(zero1, zero2)
            else:
                return -1
