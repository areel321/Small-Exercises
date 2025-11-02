# Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

def solution(st):
    # find if string is a palindrome
    if st == st[::-1]:
        return st
    
    # find smallest palindrome
    # use two pointers, one at start and one at end
    # find where pointer 1 is the same as last pointer
    '''
    pointer1 = 0
    pointer2 = len(st)-1
    pal = ""
    while pointer1 < pointer2:
        if st[pointer1] == st[pointer2]:
            pointer1 += 1
            pointer2 -=1
        else:
            pal = pal + (st[pointer1])
            pointer1 +=1
    pal = pal[::-1]
    solution = st + pal
    return solution
    '''
    # find palindrome within string input
    
    # try cutting off letters at front until we find a substr palindrome
    for i in range(0,len(st)): 
        sub = st[i:] # potential sub palindrome
        if sub == sub[::-1]: # if palindrome is found
            pre = st[:i] # find char before palindrome
            break
   
    pre = pre[::-1] # reverse char before palindrome
    solution = st+pre # append to end of solution str
    return solution
        
