'''
Remember the Microsoft Paint bucket tool? You click on a closed off area and it fills the whole thing with the colour you have selected? Looked something like this:



Let’s build it ourselves.

Input: A 2d matrix of pixels representing the canvas, a coordinate for where to start (the pixel that got clicked), and the new colour we want to use
Output: The matrix with the original pixel and all of the pixels in a continuous region that are the same colour as that original pixel turned into the new colour. Adjacency is defined as up/down/left/right, not diagonal.
'''

def solution(graph, r, c, new_colour):
   
    point = [r,c]
    old_color = graph[point[0]][point[1]]
    neighbors = []
    visited = []
    neighbors.append(point)
    
    while neighbors:
        length = len(neighbors)
        print(neighbors)
        for i in range(0, length):
            point = neighbors.pop(0)
            if graph[point[0]][point[1]] == old_color:
                graph[point[0]][point[1]] = new_colour
                
            visited.append(point)
            
            if point[1] > 0:
                left = [point[0],point[1]-1]
                # print("left", left)
                if left not in visited and graph[left[0]][left[1]] == old_color:
                    neighbors.append(left)
            if point[1] < len(graph[0])-1:
                right = [point[0], point[1]+1]
                # print("right", right)
                if right not in visited and graph[right[0]][right[1]] == old_color:
                    neighbors.append(right)
            if point[0] > 0:
                up = [point[0]-1, point[1]]
                # print("up", up)
                if up not in visited and graph[up[0]][up[1]] == old_color:
                    neighbors.append(up)
            if point[0] < len(graph)-1:
                bottom = [point[0]+1, point[1]]
                # print("b", bottom)
                if bottom not in visited and graph[bottom[0]][bottom[1]] == old_color:
                    neighbors.append(bottom)
        
    
    
    return graph
    
    
