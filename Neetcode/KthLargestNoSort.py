class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = [0]*(1+2*(10**4))
        for n in nums:
            freq[n+(10**4)] += 1
        for i in range(len(freq)-1,-1,-1):
            if freq[i] < k:
                k -= freq[i]
            else:
                return i-(10**4)
