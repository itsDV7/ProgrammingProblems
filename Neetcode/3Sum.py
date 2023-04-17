from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = set()
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums[i+1:]):
                req = 0 - (num1 + num2)
                if req in count:
                    if req == num1 or req == num2:
                        if req == 0:
                            if count[req] > 2:
                                ans.add(tuple(sorted([num1, num2, req])))
                        else:
                            if count[req] > 1:
                                ans.add(tuple(sorted([num1, num2, req])))
                    else:
                        ans.add(tuple(sorted([num1, num2, req])))
        return list(ans)
