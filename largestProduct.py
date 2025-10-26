# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def solution(inputArray):
    
    largest_input = inputArray[0]*inputArray[1] # holds the largest input so far
    for i in range(0,len(inputArray)-1):
        if (inputArray[i]*inputArray[i+1]) > largest_input:
            largest_input = inputArray[i]*inputArray[i+1]
    return largest_input
