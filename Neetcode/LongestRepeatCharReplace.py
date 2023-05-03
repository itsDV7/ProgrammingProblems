class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l = 0
        r = 0
        maxfreq = 0
        maxlen = 0
        while r < len(s):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxfreq = max(maxfreq, count[s[r]])
            if r-l+1 - maxfreq <= k:
                maxlen = max(maxlen, r-l+1)
            else:
                while r-l+1 - maxfreq > k:
                    count[s[l]] -= 1
                    l += 1
            r += 1
        return maxlen
