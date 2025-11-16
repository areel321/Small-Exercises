# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def solution(picture):
    
    # get length of strings
    length = len(picture[0])
    newArr = []
    borders = ""
    for i in range(0,length+2):
        borders += "*"
        
    print(borders)
    # add border top
    newArr.append(borders)
    
    # loop through arr
    for i in picture:
        # add * boarders aroung each str
        new = "*" + i +"*"
        newArr.append(new)
    
    # add border bottom
    newArr.append(borders)
    
    return newArr
