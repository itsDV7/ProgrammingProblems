class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = dict()
        left = 0
        right = 0
        maxfreq = 0
        maxlen = 0
        while right < len(answerKey):
            count[answerKey[right]] = 1 + count.get(answerKey[right], 0)
            maxfreq = max(maxfreq, count[answerKey[right]])
            # print(count)
            if right-left+1 - maxfreq <= k:
                maxlen = max(maxlen, right-left+1)
            else:
                while right-left+1 - maxfreq > k:
                    count[answerKey[left]] -= 1
                    left += 1
            right += 1
        return maxlen
