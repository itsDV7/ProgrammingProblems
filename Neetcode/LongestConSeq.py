class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_seq = 0
        for n in hashset:
            if n-1 not in hashset:
                curr_seq = 0
                while n+curr_seq in hashset:
                    curr_seq += 1
                max_seq = max(max_seq, curr_seq)
        return max_seq
