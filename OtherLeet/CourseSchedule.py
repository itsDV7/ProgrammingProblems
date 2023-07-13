class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [None]*numCourses
        courseSet = set()
        for frm, to in prerequisites:
            if (min(frm, to), max(frm, to)) not in courseSet:
                courseSet.add((min(frm, to), max(frm, to)))
            else:
                return False
            if frm == to:
                return False
            courses[to] = frm
            if courses[to] == courses[frm]:
                return False
        print(courses)
        for i in range(numCourses):
            if courses[i] is None:
                continue
            slow = i
            fast = i
            while slow is not None and fast is not None:
                slow = courses[slow]
                fast = courses[fast]
                if fast is not None:
                    fast = courses[fast]
                if slow == fast:
                    return False
        print("OUT")
        return True
