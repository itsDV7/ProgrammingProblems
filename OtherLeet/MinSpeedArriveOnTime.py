from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        left = 1
        right = 10**7
        min_speed = 10**7 + 1
        while left <= right:
            mid = left + (right - left)//2
            time = 0
            for i, d in enumerate(dist):
                if i < len(dist) - 1:
                    time += ceil(d/mid)
                else:
                    time += d/mid
            if time <= hour:
                min_speed = min(min_speed, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_speed
