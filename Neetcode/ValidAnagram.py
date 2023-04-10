from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ls = list(s)
        # lt = list(t)
        # if len(ls) != len(lt):
        #     return False
        # sc = Counter(ls)
        # tc = Counter(lt)
        # for k,v in sc.items():
        #     if tc[k] != v:
        #         return False
        # return True
        return Counter(s) == Counter(t)
