class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        pali = list()
        for char in s:
            if 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
                pali.append(char)
        l=0
        r=len(pali)-1
        while l!=r and l<r:
            if pali[l] != pali[r]:
                return False
            l += 1
            r -= 1
        return True
