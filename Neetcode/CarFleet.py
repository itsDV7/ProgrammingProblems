class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        spd = dict(zip(position, speed))
        position.sort(reverse=True)
        stack = []

        for p in position:
            s = (target-p)/spd[p]
            if not stack:
                stack.append(s)
            else:
                if stack[-1] < s:
                    stack.append(s)

        print(stack)
        return len(stack)
