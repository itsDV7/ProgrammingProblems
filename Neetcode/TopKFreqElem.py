from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = Counter(nums)
        return sorted(dct, key=dct.get)[-k:]
