class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = collections.Counter(s1)
        l = 0
        r = 0
        s2count = dict()
        while r <= len(s2)-len(s1):
            if s2[r] in s1count:
                l = r
                if s1count == collections.Counter(s2[l:r+len(s1)]):
                    return True
            r += 1
        return False   
