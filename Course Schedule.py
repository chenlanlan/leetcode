class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
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
                    flag = True
            for x in removeList:
                courses.remove(x)
        return len(courses) == 0