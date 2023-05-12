class TimeMap:

    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = list([(value, timestamp)])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        if key not in self.timemap:
            return ""
        right = len(self.timemap[key]) - 1
        if len(self.timemap[key]) == 0:
            return ""
        while left <= right:
            mid = left + (right - left)//2
            if self.timemap[key][mid][1] == timestamp:
                return self.timemap[key][mid][0]
            if left == mid or right == mid:
                if self.timemap[key][left][1] < timestamp < self.timemap[key][right][1]:
                    return self.timemap[key][left][0]
                elif self.timemap[key][right][1] < timestamp:
                    return self.timemap[key][right][0]
            if self.timemap[key][mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return ""
                    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
