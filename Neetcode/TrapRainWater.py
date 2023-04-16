from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        for h in height:
            if not leftMax:
                leftMax.append(h)
            else:
                if leftMax[-1] <= h:
                    leftMax.append(h)
                else:
                    leftMax.append(leftMax[-1])
        for h in height[::-1]:
            if not rightMax:
                rightMax.append(h)
            else:
                if rightMax[-1] <= h:
                    rightMax.append(h)
                else:
                    rightMax.append(rightMax[-1])
        water = 0
        n = len(height) - 1 
        for i, h in enumerate(height):
            water += min(leftMax[i], rightMax[n-i]) - h
        return water
