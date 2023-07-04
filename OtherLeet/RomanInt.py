class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0
        i = 0
        while i < len(s):
            first = s[i]
            if i == len(s) - 1:
                ans += romans[first]
                return ans
            second = s[i+1]
            print(first, romans[first], second, romans[second])
            if romans[first] < romans[second]:
                ans += romans[second] - romans[first]
                if i == len(s) - 2:
                    return ans
                i += 1
            else:
                ans += romans[first]
            i += 1
        return ans
