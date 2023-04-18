class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            if stack:
                if t <= stack[-1]:
                    stack.append(t)
                    index.append(i)
                else:
                    while stack and (t > stack[-1]):
                        res[index[-1]] = i-index[-1]
                        stack.pop()
                        index.pop()
                    stack.append(t)
                    index.append(i)
            else:
                stack.append(t)
                index.append(i)
        return res
