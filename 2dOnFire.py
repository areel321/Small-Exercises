'''
Uh oh, a node in our 2D matrix is on fire. Every second, the fire will spread to each of its neighbouring nodes (unless those nodes are just a bunch of rocks, represented by 'X'). Neighbouring here is defined as up/down/left/right, not diagonal.

Given a matrix filled with '.' (flammable) and 'X' (not flammable) and the starting point of the fire, update all the flammable nodes with the number of seconds it will take for the fire to get to them. If the fire will never reach a particular node, that node can remain marked with a '.'
'''

def solution(graph, start_r, start_c):
    point = [start_r, start_c]  
    neighbors = []
    visited = []
    neighbors.append(point)
    seconds = 0
    
    while neighbors:
        length = len(neighbors)
        print(neighbors)
        for i in range(0, length):
            point = neighbors.pop(0)
            if graph[point[0]][point[1]] == ".":
                graph[point[0]][point[1]] = str(seconds)
                
            visited.append(point)
            
            if point[1] > 0:
                left = [point[0],point[1]-1]
                # print("left", left)
                if left not in visited and graph[left[0]][left[1]] != "X":
                    neighbors.append(left)
            if point[1] < len(graph[0])-1:
                right = [point[0], point[1]+1]
                # print("right", right)
                if right not in visited and graph[right[0]][right[1]] != "X":
                    neighbors.append(right)
            if point[0] > 0:
                up = [point[0]-1, point[1]]
                # print("up", up)
                if up not in visited and graph[up[0]][up[1]] != "X":
                    neighbors.append(up)
            if point[0] < len(graph)-1:
                bottom = [point[0]+1, point[1]]
                # print("b", bottom)
                if bottom not in visited and graph[bottom[0]][bottom[1]] != "X":
                    neighbors.append(bottom)
        seconds +=1
        
    
    
    return graph
    
    

'''
def solution(graph, start_r, start_c):
    
    # find start point
    # visit neighbors, update flamable
    # keep a counter of seconds, each time we search neighbors a second is added
    seconds = 0
    point = [start_r, start_c]
    visited = []
    g = helper(graph, point, seconds, visited)
    
    return g
    
    
def helper(graph, point, seconds, visited):
    visited.append(point)
    
    if graph[point[0]][point[1]] == ".":
        graph[point[0]][point[1]]  = str(seconds)
    if graph[point[0]][point[1]]  == "X":
        return graph
    #vist left
    if point[1] > 0:
        left = [point[0],point[1]-1]
        # print("left", left)
        if left not in visited and graph[left[0]][left[1]] != "X":
            helper(graph, left, seconds, visited)
    if point[1] < len(graph[0])-1:
        right = [point[0], point[1]+1]
        # print("right", right)
        if right not in visited and graph[right[0]][right[1]] != "X":
            helper(graph, right, seconds, visited)
    if point[0] > 0:
        up = [point[0]-1, point[1]]
        # print("up", up)
        if up not in visited and graph[up[0]][up[1]] != "X":
            helper(graph, up, seconds, visited)
    if point[0] < len(graph)-1:
        bottom = [point[0]+1, point[1]]
        # print("b", bottom)
        if bottom not in visited and graph[bottom[0]][bottom[1]] != "X":
            helper(graph, bottom, seconds, visited)
    
    
    return graph
    '''
     
                    

