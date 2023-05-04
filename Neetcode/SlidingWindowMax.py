from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = list()
        dq = deque()
        
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        for i in range(k, len(nums)):
            ans.append(nums[dq[0]])
            while dq and i-k >= dq[0]:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        
        if dq:
            ans.append(nums[dq[0]])
        
        return ans
