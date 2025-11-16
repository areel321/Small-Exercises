def solution(graph, r, c, new_colour):
   
    point = [r,c]
    old_color = graph[point[0]][point[1]]
    neighbors = []
    neighbors.append(point)
    visited = []
    
    while neighbors:
        point = neighbors.pop(0)
        visited.append(point)
        if graph[point[0]][point[1]] == old_color:
            graph[point[0]][point[1]] = new_colour
        print(graph)
        if point[1] > 0:
            left = [point[0],point[1]-1]
            # print("left", left)
            if point not in visited:
                neighbors.append(left)
        if point[1] < len(graph[0])-1:
            right = [point[0], point[1]+1]
            # print("right", right)
            if point not in visited:
                neighbors.append(right)
        if point[0] > 0:
            up = [point[0]-1, point[1]]
            # print("up", up)
            if point not in visited:
                neighbors.append(up)
        if point[0] < len(graph)-1:
            bottom = [point[0]+1, point[1]]
            # print("b", bottom)
            if point not in visited:
                neighbors.append(bottom)
    
    
    print(graph)
    return graph
    
    
    

solution([["#FFF","#FFF","#FFF","#000","#000","#000","#000"], 
 ["#FFF","#FFF","#FFF","#000","#000","#000","#000"], 
 ["#000","#000","#000","#000","#000","#000","#000"], 
 ["#000","#FFF","#FFF","#000","#000","#000","#000"], 
 ["#FFF","#FFF","#FFF","#000","#000","#000","#000"]], 1, 1, "#A1F")