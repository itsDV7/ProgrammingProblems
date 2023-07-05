class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lenarr = list()
        count = 0
        maxlen = 0
        for n in nums:
            if n == 0:
                if count:
                    lenarr.append(count)
                    maxlen = max(maxlen, count)
                    count = 0
                lenarr.append(count)
            else:
                count += 1
        if count:
            lenarr.append(count)
        if len(lenarr) == 1:
            if lenarr[0]:
                return lenarr[0] - 1
            else:
                return 0
        if len(lenarr) == 2:
            return maxlen
        for i in range(len(lenarr)-2):
            curr = lenarr[i]
            next = lenarr[i + 2]
            maxlen = max(maxlen, curr + next)
        # print(lenarr)
        return maxlen
