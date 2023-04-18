class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(["+", "-", "*", "/"])
        for t in tokens:
            if t not in op:
                stack.append(int(t))
            else:
                numR = int(stack.pop())
                numL = int(stack.pop())
                if t == "+":
                    stack.append(numL + numR)
                elif t == "-":
                    stack.append(numL - numR)
                elif t == "*":
                    stack.append(numL * numR)
                elif t == "/":
                    stack.append(int(numL / numR))
        return stack[-1]
