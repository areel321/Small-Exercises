'''
https://leetcode.com/problems/cherry-pickup/?envType=problem-list-v2&envId=matrix
741. Cherry Pickup
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
'''

# graph
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        
        cherries = 0

        # right or down
        visited = []
        q = []
        start_point = [0,0]
        point = start_point
        q.append(point)

        while q:
            length = len(q)
            for i in range(0, length):
                point = q.pop(0)
                if grid[point[0]][point[1]] == 1:
                    cherries = cherries + 1
                    grid[point[0]][point[1]] = 0
                visited.append(point)

                # bottom 
                if point[0] < len(grid)-1:
                    bottom = [point[0]+1, point[1]]
                    if bottom not in visited and grid[bottom[0]][bottom[1]] != -1:
                        q.append(bottom)
                
                # right
                if point[1] < len(grid)-1:
                    right = [point[0], point[1]+1]
                    if right not in visited and grid[right[0]][right[1]] != -1:
                        q.append(right)

        max_point = [len(grid)-1, len(grid[0])-1]
        if max_point not in visited:
            return 0

        # left or top
        visited = []
        q = []
        point = [len(grid)-1, len(grid[0])-1]
        q.append(point)
        cherries2 = 0

        while q:
            length = len(q)
            for i in range(0, length):
                point = q.pop(0)
                if grid[point[0]][point[1]] == 1:
                    cherries2 = cherries2 + 1
                    grid[point[0]][point[1]] = 0
                visited.append(point)

                # top
                if point[0] > 0:
                    top = [point[0]-1, point[1]]
                    if top not in visited and grid[top[0]][top[1]] != -1:
                        q.append(top)
                # left
                if point[1] > 0:
                    left = [point[0], point[1]-1]
                    if left not in visited and grid[left[0]][left[1]] != -1:
                        q.append(left)

        print(cherries, cherries2, visited)
        if start_point in visited:
            return cherries + cherries2
        else:
            return cherries
        
