'''
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=sorting
'''
# trick
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1&nums2)

'''
# no trick
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums1:
            if i in nums2 and i not in l:

                l.append(i)
        return l
'''       
        
