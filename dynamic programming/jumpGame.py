'''
55. Jump Game
https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=dynamic-programming
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''
class Solution(object):
    '''
    DP definition: The farthest index we can reach given allowed steps from 0 to i
DP decision & relationship: It's either the dp[i - 1] or i + nums[i] whichever one is larger
DP condition:
If at any moment, dp[i] = 0, that means there is no way it can reach any further, return False immediately.
If at any moment, dp[i] >= last index, that means it can already reach the end of the array given the steps allowed from 0 to i, return True immediately.
'''

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        arr = [0] * len(nums)

        arr[0] = nums[0]

        for i in range(0,len(nums)-1):
            if arr[i-1] < i:
                return False 
            arr[i] = max(i+nums[i], arr[i-1])
            if arr[i] >= len(nums)-1:
                return True
        return arr[len(nums)-2]>= len(nums)-1




'''
class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if we are at or over the length of nums, return true
        # otherwise, try each jump up to max jump
        return self.helper(nums, 0, nums[0])
        
        
    def helper(self, nums, pos, jump):
        #check
        if (pos >= len(nums)-1):
            print("i'm here")
            return True

        for i in range(1, jump + 1):
            npos = pos + i
            if self.helper(nums, npos, nums[npos]):
                return True
        return False
    '''   
