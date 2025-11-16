# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

def solution(matrix):
    new = []
    
    for i in range(0,len(matrix)):
        row = []
        for j in range(0,len(matrix[i])):
            row.append(0)
        new.append(row)
    # print(new)
    #going to use search
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            point = [i,j]
            # print(point)
            neighbors = []
            if point[1] > 0:
                left = matrix[point[0]][point[1]-1]
                # print("left", left)
                neighbors.append(left)
                if left == True:
                    new[i][j] +=1
            if point[1] < len(matrix[i])-1:
                right = matrix[point[0]][point[1]+1]
                neighbors.append(right)
                # print("right", right)
                if right == True:
                    new[i][j] +=1
            if point[0] > 0:
                up = matrix[point[0]-1][point[1]]
                neighbors.append(up)
                # print("up", up)
                if up == True:
                    new[i][j] +=1
            if point[0] < len(matrix)-1:
                bottom = matrix[point[0]+1][point[1]]
                neighbors.append(bottom)
                # print("b", bottom)
                if bottom == True:
                    new[i][j] +=1
                    
            #diagonal neighbors
            if (point[0] > 0) and (point[1] > 0):
                d_up_left = matrix[point[0]-1][point[1]-1]
                neighbors.append(d_up_left)
                if d_up_left == True:
                    new[i][j] +=1
            if (point[0] > 0) and (point[1] < len(matrix[i])-1):
                d_up_right = matrix[point[0]-1][point[1]+1]
                neighbors.append(d_up_right)
                if d_up_right == True:
                    new[i][j] +=1
            if (point[0] < len(matrix)-1) and (point[1] > 0):
                d_b_left = matrix[point[0]+1][point[1]-1]
                neighbors.append(d_b_left)
                if d_b_left == True:
                    new[i][j] +=1
            if (point[0] < len(matrix)-1) and (point[1] < len(matrix[i])-1):
                d_b_right = matrix[point[0]+1][point[1]+1]
                neighbors.append(d_b_right)
                if d_b_right == True:
                    new[i][j] +=1
                
            '''
            print(neighbors)
            for x in neighbors:
                if x == True:
                    new[i][j] +=1
            '''
            
                
    return new
        
