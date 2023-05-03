from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left_min = deque()
        # right_max = deque()
        # for i in range(len(prices)):
        #     if left_min:
        #         left_min.append(min(left_min[-1], prices[i]))
        #     else:
        #         left_min.append(prices[i])
        #     if right_max:
        #         right_max.appendleft(max(right_max[0], prices[len(prices)-1-i]))
        #     else:
        #         right_max.appendleft(prices[len(prices)-1-i])
        # print(left_min)
        # print(right_max)

        # i=0
        # profit = 0
        # while (i<len(prices)-1):
        #     if left_min[i] < right_max[i + 1]:
        #         profit = max(profit, right_max[i + 1] - left_min[i])
        #     i += 1
        # return profit
        l=0
        r=1
        profit = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
