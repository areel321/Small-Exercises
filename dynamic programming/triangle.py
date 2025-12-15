120. Triangle
https://leetcode.com/problems/triangle/description/?envType=problem-list-v2&envId=dynamic-programming
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if len(triangle) < 1:
            return triangle
        elif len(triangle) == 1:
            return triangle[0][0]

        level = 0
        total = 0
        
        
        t = self.helper(triangle, level, total)
        print(t)
        return t
            
    def helper(self, triangle, level, total):
        print(level, total)
        if level == len(triangle):
            print(total)
            return total
        else:
            curr = sorted(triangle[level])
            total += curr[0]
            level+=1
            return self.helper(triangle, level, total)
'''
