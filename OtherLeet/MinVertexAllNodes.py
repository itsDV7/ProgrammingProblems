class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodeset = set()
        ans = list()
        for f, t in edges:
            nodeset.add(t)
        for i in range(n):
            if i not in nodeset:
                ans.append(i)
        return ans
