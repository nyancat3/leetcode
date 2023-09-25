class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        left_sum = [0] * len(maxHeights)
        monotonic_stack = [] # increasing
        sum = 0
        for i, height in enumerate(maxHeights):
            popped_count = 0
            while monotonic_stack and monotonic_stack[-1][0] > height:
                h, count = monotonic_stack.pop()
                sum -= h * count
                popped_count += count
            monotonic_stack.append([height, popped_count + 1])
            sum += height * (popped_count + 1)
            left_sum[i] = sum - height # subtract the current height
            # print(sum)
            # print(left_sum)
            # print(monotonic_stack)

        right_sum = [0] * len(maxHeights)
        sum, ans = 0, 0
        monotonic_stack = []
        for i, height in reversed(list(enumerate(maxHeights))):
            popped_count = 0
            while monotonic_stack and monotonic_stack[-1][0] > height:
                h, count = monotonic_stack.pop()
                sum -= h * count
                popped_count += count
            monotonic_stack.append([height, popped_count + 1])
            sum += height * (popped_count + 1)
            right_sum[i] = sum - height # subtract the current height
            ans = max(ans, left_sum[i] + height + right_sum[i])
            # print(sum)
            # print(right_sum)
            # print(monotonic_stack)
        return ans
