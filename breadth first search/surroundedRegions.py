'''
https://leetcode.com/problems/surrounded-regions/?envType=problem-list-v2&envId=matrix
130. Surrounded Regions
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
'''

# graph dfs
# https://leetcode.com/problems/surrounded-regions/solutions/6594858/beginner-friendly-dfs-solution-java-c-py-v2kd
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # if all cells on boarders
        if len(board)<3 or len(board[0])<3:
            return

        visited = []

        for i in range(len(board[0])-1):
            if board[0][i] == 'O':
                self.helper([0,i], visited, board)
        for i in range(len(board)-1):
            if board[i][0] == 'O':
                self.helper([i,0], visited, board)
        for i in range(len(board[0])):
            if board[len(board)-1][i] == 'O':
                self.helper([len(board)-1, i], visited, board)
        for i in range(len(board)):
            if board[i][len(board[0])-1] == 'O':
                self.helper([i,len(board[0])-1], visited, board)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and [i,j] not in visited:
                    board[i][j] = 'X'

    def helper(self, point, visited, board):
        print(point)
        if board[point[0]][point[1]] == 'X' or point in visited:
            return
        visited.append(point)
        # bottom 
        if point[0] < len(board)-1:
            bottom = [point[0]+1, point[1]]
            self.helper(bottom, visited, board)
        # right
        if point[1] < len(board[0])-1:
            right = [point[0], point[1]+1]
            print(right)
            self.helper(right, visited, board)
        # left
        if point[1] > 0:
            left = [point[0], point[1]-1]
            self.helper(left, visited, board)
        # top
        if point[0] > 0:
            top = [point[0]-1, point[1]]
            self.helper(top, visited, board)

            
