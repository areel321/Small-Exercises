# import requests
# import mysql.connector
# import pandas as pd

# An island is all of the land that connects top-bottom or left-right. For example, in this grid:

#  0 1 0 1 1 0
#  1 1 0 1 0 0
#  0 1 1 0 1 1
# there are three distinct islands with these shapes:

#    1        1 1
#  1 1        1
#    1 1               1 1
# Return the area of the largest island


# Expected output: 5

def findLargestIsland(grid):
    
    islands = [] # 0, 
    
    for i in grid:
        for j in grid[i]:
            islands.append(helper(grid, (i, j), set(), 0))
    
    return max(islands)
    
    


def helper(grid, point, seen_points, curr_island): # _, 2,1, {(0,1),(1,1), (2,1)}, 2
    # point = [5, 0]
    if point == 0:
        return curr_island # 2
    else:
        if point in seen_points:
            return curr_island # 0
        else:
            seen_points.append(point) # (0, 1), (1,1)
            # visit neighbors - TODO fix edge cases
            if point[0] != 0: 
                left = [point[0] - 1 , point[1]] # 4, 0
                if grid[left] == 1:
                    curr_island += 1
                    helper(grid, left, seen_points, curr_island) # 2
                    
            if point[0] != len(grid[0])-1:
                right = [point[0] + 1, point[1]] # 2,1
                if grid[right] == 1: 
                    curr_island += 1 # 2
                    helper(grid, right, seen_points, curr_island) #grid, (2,1), {(0,1), (1,1)}, 2 => 2
                
            if point[1] != 0:
                up = [point[0], point[1] - 1] #  1, 0
                if grid[up] == 1:
                    curr_island += 1 # 2
                    helper(grid, left, seen_points, curr_island) # grid, (1,0), {(0,1), (1,1), (2,1)}, 2
             
            if point[1] != len(grid)-1:
                down = [point[0], point[1] + 1] # 1, 2
                if grid[down] == 1:
                    curr_island += 1
                    helper(grid, left, seen_points, curr_island)
