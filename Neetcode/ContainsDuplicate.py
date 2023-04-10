class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
          
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         dct = {}
#         for n in nums:
#             if n in dct.keys():
#                 return True
#             else:
#                 dct[n] = True
#         return False
