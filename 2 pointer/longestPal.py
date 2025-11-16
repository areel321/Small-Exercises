# import requests
# import mysql.connector
# import pandas as pd

# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# qracecars

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Check each point as middle of pal
        # either 2 char or 3 char
        # then check if further expansion points are equal to create a larger pal
        
        # check each middle point until a pal is found
        if len(s) > 0:
            longest_pal = s[0]
        elif len(s) == 0:
            return 0
        pal = ""
        # Odd length palindromes
        for i in range(1, len(s)):
            left = i-1
            right = i+1
            while left>=0 and right<=len(s)-1 and s[left] == s[right]:
                pal = s[left:right+1]
                left -=1
                right +=1
            
            
            print(left, right, pal)
            if len(pal) > len(longest_pal):
                longest_pal = pal
                
        # Even length palindromes
        for i in range(0, len(s)):
            left = i
            right = i+1
            while left>=0 and right<=len(s)-1 and s[left] == s[right]:
                pal = s[left:right+1]
                left-=1
                right+=1
           
            print(left, right, pal)
            if len(pal) > len(longest_pal):
                longest_pal = pal
                
        return longest_pal
