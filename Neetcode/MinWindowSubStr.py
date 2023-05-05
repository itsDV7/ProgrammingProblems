class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = collections.Counter(t)
        l = 0
        r = 0
        ans = ""
        scount = dict()
        minsub = len(s) + 1
        tchars = len(tcount)
        schars = 0
        while r < len(s):
            if s[r] in tcount:
                if s[r] in scount:
                    scount[s[r]] += 1
                else:
                    scount[s[r]] = 1
                if scount[s[r]] == tcount[s[r]]:
                    schars += 1
            # print(tchars, schars)
            while schars == tchars:
                while s[l] not in tcount:
                    l += 1
                if r-l+1 < minsub:
                    minsub = r-l+1
                    ans = s[l:r+1]
                # minsub = min(minsub, r-l+1)
                # ans = s[l:r+1]
                if s[l] in tcount:
                    scount[s[l]] -= 1
                    if scount[s[l]] < tcount[s[l]]:
                        schars -= 1
                l += 1

            r += 1

        return ans
