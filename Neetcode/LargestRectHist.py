class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index = []
        height = []
        area = 0
        
        for i, h in enumerate(heights):
            if not height:
                height.append(h)
                index.append(i)
            else:
                if h >= height[-1]:
                    height.append(h)
                    index.append(i)
                else:
                    while height and h < height[-1]:
                        area = max(area, height[-1]*(i-index[-1]))
                        height.pop()
                        last_in = index.pop()
                    height.append(h)
                    index.append(last_in)
                    # height[-1] = h
            
            # print(i, h, index, height, area)

        # print(index, height, area)

        while height:
            area = max(area, height[-1]*(len(heights) - index[-1]))
            height.pop()
            index.pop()
            # print(index, height, area)

        # print(index, height, area)

        return area
