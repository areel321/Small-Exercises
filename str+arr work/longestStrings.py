# Given an array of strings, return another array containing all of its longest strings.
def solution(inputArray):
    longestStrLen = 0 # length of the longest string
    longestStrs = [] # arr to hold all the longest strings
    longest = {} # dict to hold length, strings pairs
    
    '''
    for i in inputArray:
        length = len(i)
        if length > longestStrLen:
            longestStrLen = length
    print(longestStrLen)
    for i in inputArray:
        if len(i) == longestStrLen:
            longestStrs.append(i)
            
    return longestStrs
    '''
    
    for i in inputArray:
        if len(i) in longest.keys():
            longest[len(i)].append(i)
        else:
            longest[len(i)] = [i]
        
    longestStrLen = max(longest)
    return longest[longestStrLen]
