from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        scount = Counter(s)
        goalcount = Counter(goal)
        if s == goal:
            for k, v in scount.items():
                if v > 1:
                    return True
            return False
        else:
            if scount != goalcount:
                return False
            hits = 0
            for i in range(len(s)):
                if s[i] != goal[i]:
                    hits += 1
                if hits > 2:
                    return False
            if hits == 2:
                return True
        return False
    
