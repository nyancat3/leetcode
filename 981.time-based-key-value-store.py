#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:
    def __init__(self):
        self.vals = defaultdict(list)
        self.times = defaultdict(list) # increasing order

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(value)
        self.times[key].append(timestamp)
        print(self.vals)
        print(self.times)

    def get(self, key: str, timestamp: int) -> str:
        times = self.times[key]
        l, r = 0, len(times) - 1
        res_index = -1
        max_time = -1
        while l <= r:
            m = (l + r) // 2
            if times[m] == timestamp:
                return self.vals[key][m]
            elif times[m] < timestamp:
                if max_time < times[m]:
                    max_time = times[m]
                    res_index = m
                l = m + 1   # move to the right
            else:
                r = m - 1   # move to the left
        return self.vals[key][res_index] if res_index != -1 else ""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
