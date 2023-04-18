class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in list(s):
            if len(stack):
                if stack[-1] == "(" and c == ")":
                    stack.pop()
                elif stack[-1] == "[" and c == "]":
                    stack.pop()
                elif stack[-1] == "{" and c == "}":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        if len(stack):
            return False
        else:
            return True
