'''
198 house robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

[9,7,11,12,52,85,100,12,13,2,5,1,40]
max up to 5 - 150
max up to 1 - 150

Logan Castrucci
11:51 AM
[9,7,11,12,52]
Max of 9,7 = 9
Max of 9,7,11 = 9 + 11 = 20
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # max of current + (current-1 + current-3 or current-2)
        # max of (current + up to previous-2) or (previous-1)


        
    def helper(self, nums, cache):
        #check
        if len(nums) == 1: # at the end
            return nums[0]
        n = len(nums)
        m = nums[n-1]
        return max( (self.helper(nums[:n-1], cache)), (m + self.helper(nums[:n-2], cache)))
        
