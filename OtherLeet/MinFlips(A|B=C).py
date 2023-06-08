class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a).lstrip("0b")
        b = bin(b).lstrip("0b")
        c = bin(c).lstrip("0b")

        count = 0

        for i in range(-1, min([-1*len(a), -1*len(b), -1*len(c)])-1, -1):
            if i >= -1*len(a) and i >= -1*len(b) and i >= -1*len(c):
                if c[i] == "1":
                    if a[i] == "0" and b[i] == "0":
                        count += 1
                elif c[i] == "0":
                    if a[i] == "1" and b[i] == "1":
                        count += 2
                    elif a[i] == "1" or b[i] == "1":
                        count += 1
            elif i >= -1*len(a) and i >= -1*len(b):
                if a[i] == "1" and b[i] == "1":
                    count += 2
                elif a[i] == "1" or b[i] == "1":
                    count += 1
            elif i >= -1*len(a) and i >= -1*len(c):
                if a[i] != c[i]:
                    count += 1
            elif i >= -1*len(b) and i >= -1*len(c):
                if b[i] != c[i]:
                    count += 1
            elif i >= -1*len(a):
                if a[i] == "1":
                    count += 1
            elif i >= -1*len(b):
                if b[i] == "1":
                    count += 1
            elif i >= -1*len(c):
                if c[i] == "1":
                    count += 1
            
        return count
