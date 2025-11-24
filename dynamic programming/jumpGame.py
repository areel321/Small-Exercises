'''
55. Jump Game
https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=dynamic-programming
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
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
        
