class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        else:
            p1 = coordinates[0]
            p2 = coordinates[1]
            
            if p1[0] == p2[0]:
                for i in range(2, len(coordinates)):
                    p = coordinates[i]
                    if p[0] != p1[0]:
                        return False
                return True
            
            m = (p2[1] - p1[1])/(p2[0] - p1[0])
            c = p1[1] - (m * p1[0])
            for i in range(2, len(coordinates)):
                p = coordinates[i]
                if p[1] != ((m * p[0]) + c):
                    return False
            return True
