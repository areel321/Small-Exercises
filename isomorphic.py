# Two two-dimensional arrays are isomorphic if they have the same number of rows and each pair of respective rows contains the same number of elements.
# Given two two-dimensional arrays, check if they are isomorphic.

def solution(array1, array2):
    
    # need to find if num rows are equal
    # find if elements in each respective row are equal
    
    # find if length is equal
    len1 = len(array1)
    len2 = len(array2)
    if len1 != len2:
        return False
    
    # find if len of each sub array is equal
    for i in range(0,len1):
        len1_sub = len(array1[i])
        len2_sub = len(array2[i])
        if len1_sub != len2_sub:
            return False
            
    return True
