from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # for k, v in count.items():
        #     if v > 1:
        #         return k

        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                intersect = slow
                break

        slow = 0
        while True:
            slow = nums[slow]
            intersect = nums[intersect]
            if slow == intersect:
                break

        return slow
