from math import log
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        if limit <= 5:
            return []
        length = len(message)
        print("Len: ", length)
        left = 1
        right = length
        ans = right + 1
        while left <= right:
            mid = left + (right - left)//2
            parts = mid - 1
            print("mid: ", mid)
            minlen = 0
            if parts:
                for n in range(int(log(parts, 10))+1):
                    strlen = limit - (3 + len(str(mid)) + (n + 1))
                    if not strlen:
                        minlen = length
                        break
                    minlen += strlen * min(parts, 9 * 10 ** n)
                    parts -= 9 * 10 ** n
                    print(n, strlen, minlen, parts)
                maxlen = minlen + (limit - (3 + 2*len(str(mid))))
                minlen += 1
            else:
                minlen = 1
                maxlen = limit - 5
            print("minlen: ", minlen)
            print("maxlen: ", maxlen)
            print("\n")
            if minlen > length:
                right = mid - 1
            elif maxlen < length:
                left = mid + 1
            else:
                ans = min(ans, mid)
                left = 1
                right = mid - 1
        if ans == length + 1:
            minlen = 1
            maxlen = limit - 5
            if length <= maxlen:
                return [message + "<1/1>"]
        else:
            l = list()
            start = 0
            stop = 0
            for i in range(ans):
                suff = f"<{i+1}/{ans}>"
                stop = limit - len(suff)
                pref = f"{message[start:start+stop]}"
                l.append(pref + suff)
                start += stop
            return l
        return []
