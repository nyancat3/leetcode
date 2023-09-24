class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        final_ans = 0
        for i in range(len(maxHeights)):
            peak_height = maxHeights[i]
            left_height = min(peak_height, maxHeights[i - 1]) if i > 0 else 0
            right_height = min(peak_height, maxHeights[i + 1]) if i < len(maxHeights) - 1 else 0
            ans = peak_height
            for j in range(i - 1, -1, -1): # left side
                left_height = min(left_height, maxHeights[j])
                ans += left_height
            for j in range(i + 1, len(maxHeights)): # right side
                right_height = min(right_height, maxHeights[j])
                ans += right_height
            print(ans, i)
            final_ans = max(final_ans, ans)
        return final_ans
