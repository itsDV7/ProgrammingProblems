class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = needle[0]
        for i, h in enumerate(haystack):
            # print(h)
            if len(haystack) - i < len(needle):
                break
            if h == n:
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                else:
                    return i
        return -1
