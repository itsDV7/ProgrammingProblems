import heapq
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        right = sum(batteries[:-n])
        left = batteries[-n:]
        time = 0
        for i in range(n-1):
            if right//(i+1) < left[i+1] - left[i]:
                return left[i] + right//(i+1)
            right -= (i+1) * (left[i+1] - left[i])
        return left[-1] + right//n
        # for i in range(len(batteries)):
        #     batteries[i] *= -1
        # time = 0
        # heapq.heapify(batteries)
        # while len(batteries) >= n:
            # print(batteries)
            # temp = list()
            # for i in range(n):
            #     battery = heapq.heappop(batteries)
            #     battery *= -1
            #     temp.append(battery)
            # for i in range(n):
            #     temp[i] -= 1
            # for t in temp:
            #     if t:
            #         heapq.heappush(batteries, -1 * t)
            # time += 1
            # for _ in range(n):
            #     battery = heapq.heappop(batteries)
            #     battery *= -1
            #     battery -= 1
            #     if battery:
            #         heapq.heappush(batteries, battery * -1)
            # time += 1
        # return time
