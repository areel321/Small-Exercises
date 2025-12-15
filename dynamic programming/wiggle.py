376. Wiggle Subsequence
https://leetcode.com/problems/wiggle-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = 2
        if len(nums) <= 1:
            return len(nums)
        
        prev = nums[0] - nums[1]


        for i in range(1, len(nums)-1):
            
            one = nums[i]
            two = nums[i+1]
            diff = nums[i]-nums[i+1]
            print(prev, diff)
            if prev < 0:
                if diff > 0:
                    seq +=1
                else:
                    seq = 2
            elif prev > 0:
                if diff < 0:
                    seq +=1
                else:
                    seq = 2
            prev = diff
        return seq

        
