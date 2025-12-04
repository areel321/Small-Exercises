'''
207. Course Schedule
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
https://leetcode.com/problems/course-schedule/solutions/5467172/video-topological-sort-visualization-to-es7la
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0]* numCourses
        adjList = [[] for x in range(numCourses)]

        for i in prerequisites:
            adjList[i[1]].append(i[0])
            indegree[i[0]] +=1

        queue = []
        for i in range(0,numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            n = queue.pop(0)
            visited +=1
            for neighbor in adjList[n]:
                indegree[neighbor] -=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == visited

        
