'''
https://leetcode.com/problems/flipping-an-image/description/?envType=problem-list-v2&envId=matrix
832. Flipping an Image
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
'''

# non graph
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # flip horizontally
        for i in range(0, len(image)):
            row = image[i]
            image[i] = row[::-1]
            for j in range(0, len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        
        return image
