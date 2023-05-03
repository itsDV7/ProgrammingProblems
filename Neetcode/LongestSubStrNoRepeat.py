class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        wordset = set()
        maxsize = 0
        while r < len(s):
            if wordset:
                if s[r] in wordset:
                    while s[l] != s[r]:
                        wordset.remove(s[l])
                        l += 1
                    l += 1
                else:
                    wordset.add(s[r])
            else:
                wordset.add(s[r])
            maxsize = max(maxsize, r-l + 1)
            r += 1
        return maxsize
