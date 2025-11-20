'''
You have a binary tree t. Your task is to find the largest value in each row of this tree. In a tree, a row is a set of nodes that have equal depth. For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

Return an array in which the first element is the largest value in the row with depth 0, the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    '''Initialization: Enqueue the given source vertex into a queue and mark it as visited.
    Exploration: While the queue is not empty:
    Dequeue a node from the queue and visit it (e.g., print its value).
    For each unvisited neighbor of the dequeued node:
    Enqueue the neighbor into the queue.
    Mark the neighbor as visited.
    Termination: Repeat step 2 until the queue is empty.'''
    queue = []
    if t:
        queue.append(t)
    maxes = []
    levels = [] 
    level = 0
    while queue:
        levels.append([])
        #print("queue", queue)
        l = len(queue)
        for i in range(0,l):
            
            curr  = queue.pop(0)
            #print(curr.value)
            levels[level].append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)    
        level +=1
    
    for i in levels:
        #print(i)
        maxes.append(max(i))
    return maxes
