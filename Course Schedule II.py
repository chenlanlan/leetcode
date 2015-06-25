class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def findOrder(self, numCourses, prerequisites):
        res = []
        degree = [0] * numCourses
        parents = [[] for x in range(numCourses)]
        for pair in prerequisites:
            degree[pair[1]] += 1
            parents[pair[0]].append(pair[1])
        courses = set(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degree[x] == 0:
                    for parent in parents[x]:
                        degree[parent] -= 1
                    removeList.append(x)
                    res.append(x)
                    flag = True
            for x in removeList:
                courses.remove(x)
        if len(courses) == 0:
            res.reverse()
            return res
        else:
            return []

test = Solution()
print(test.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))