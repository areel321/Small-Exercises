# Note: Your solution should have only one BST traversal and O(1) extra space complexity, since this is what you will be asked to accomplish in an interview.

# A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and the right subtrees must also be binary search trees.
# Given a binary search tree t, find the kth smallest element in it.

# Note that kth smallest element means kth element in increasing order. See examples for better understanding.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None, less
#     self.right = None, greater
def solution(t, k):
    l = []
    curr = t
    l.append(curr.value)
    helper(curr, l)
        
    l = sorted(l)
    print(l)
    return l[k-1]
    
        
        
        
    return curr.value
        
def helper(curr, l):
    if curr.left:
        l.append(curr.left.value)
        helper(curr.left, l)
    if curr.right:
        l.append(curr.right.value)
        helper(curr.right, l)
