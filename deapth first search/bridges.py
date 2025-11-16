# import requests
# import mysql.connector
# import pandas as pd

# Examples
# bridges = [[1], [0, 2, 6], [1, 3, 5], [2, 4], [3], [2, 6], [1, 5]] and a = 6, b = 4. => output = 2
# bridges = [[1], [0, 2], [1, 3, 5], [2, 4], [3], [2, 6], [5]], a = 0, b = 4 -> output = 4
# bridges = [[1, 2], [0], [0]], a = 0, b = 2 -> output = 1


# As the first step you want to calculate the number of suitable bridges. Given the bridges configuration and information about islands a and b, return the number of bridges which destruction will definitely be noted by the elders.


# paths (for complex example) = [[6,5,2,3,4], [6,1,5,2,3,4]]
# 1 - check if i (6) is in the second list/set
# 2 - check if i+1 (5) is after i in the second list/set
# [6,5,2,3,4], {2,4,3,6,1,5}
# {6:5, 5:2, 2:3, 3:4}, {6:1, 1:5, 5:2, 2:3, 3:4}

# Check if 6 is in a given list of numbers
# list => O(n)
# dictionary => O(1)
# set => O(1)

# bridges = adjacency list
def solution(bridges, a, b):
    # DFS, find each path a -> b, starting with current node a
    visited = []
    paths = []
    paths = helper(a, bridges, b, visited, paths) # 0, bridges, 2, [], []
    # find total common edges
    dicts = []
    for i in paths:
        dict_i = {}
        for j in range(0, len(i)-1):
            dict_i[i[j]] = i[j+1]
        dicts.append(dict_i)
    
    common = [] # common edge count
    for key in dicts[0].keys():
        for dictionary in dicts:
            if key in j.keys():
                if dicts[0][key] == dictionary[key]:
                    common.append[key]
                    
    return len(common)-1
                    
        
    
    
def helper(curr, bridges, b, visited, paths): # 0, bridges, 2, [0, 1]
    if curr == b: # we've reached the end of our path
        return [curr]
    if curr in visited: # we already visited this node
        return
    
    visited.append(curr) # add our current node to the path # visited  = [0, 1]
    for i in bridges[curr]: # bridges[1] = [0]
        path = helper(i, bridges, b, visited) # 2, bridges, 2, [0, 1] => [2]
        if path:
            path = path.insert(0, curr) # -> [0, 2]
            paths.append(path)
    return paths
        

