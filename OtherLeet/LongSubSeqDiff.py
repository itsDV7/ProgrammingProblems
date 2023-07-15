class Solution:
    def helper(self, index, prev, arr, diff):
        n = len(arr)
        if index >= n:
            return 0

        take = 0
        notake = 0
        if prev == -10000:
            notake = self.helper(index + 1, prev, arr, diff)
            take = 1 + self.helper(index + 1, arr[index], arr, diff)
        else:
            notake = self.helper(index + 1, prev, arr, diff)
            if arr[index] - prev == diff:
                take = 1 + self.helper(index + 1, arr[index], arr, diff)
        return max(take, notake)

    def longestSubsequence(self, arr, difference):
        n = len(arr)
        return self.helper(0, -10000, arr, difference)
