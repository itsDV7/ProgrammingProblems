from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        if len(piles) == h:
            return max(piles)
        else:
            left = 1
            right = max(piles)
            ans = right + 1
            while left <= right:
                mid = left + (right - left)//2
                time = 0
                for p in piles:
                    time += ceil(p/mid)
                if time > h:
                    left = mid + 1
                else:
                    ans = min(ans, mid)
                    right = mid - 1
            return ans
