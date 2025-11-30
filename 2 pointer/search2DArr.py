'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
import math
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # get middle and keep sectioning down on first elements of rows
        # then on our selected row
        if len(matrix) <= 1:
            return target in matrix[0]

        middle = int(math.floor(len(matrix) / 2)) # round down
        print(middle)
        lower = 0
        upper = len(matrix) - 1
        
        while upper >= lower: # diff is maybe 0 or 1
            print(upper, lower, middle)
            middle = int(math.floor((upper+lower) / 2))
            if target <= matrix[middle][0]:
                upper = middle - 1
                
            if target >= matrix[middle][0]:
                lower = middle + 1
               
        
        #assuming lower rn
        row  = int(math.floor((upper+lower) / 2))
        print(row)
        upper = len(matrix[row]) - 1
        lower = 0
        middle = int(math.floor((upper+lower) / 2))
        
        while upper >= lower:
            middle = int(math.floor((upper+lower) / 2))
            print("2nd", upper, lower, middle)
            print(matrix[row][middle])
            if target == matrix[row][middle]:
                return True

            if target < matrix[row][middle]:
                upper = middle - 1
                
            if target > matrix[row][middle]:
                lower = middle + 1
                
            
        return False
        
