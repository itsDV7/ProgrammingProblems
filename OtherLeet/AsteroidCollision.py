class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = list()
        ast = 0
        while ast < len(asteroids):
            if not res:
                res.append(asteroids[ast])
            else:
                while res and (res[-1] >= 0 and asteroids[ast] < 0):
                    if res[-1] < abs(asteroids[ast]):
                        res.pop()
                    elif res[-1] == abs(asteroids[ast]):
                        res.pop()
                        break
                    else:
                        break
                else:
                    res.append(asteroids[ast])
            ast += 1
        return res
