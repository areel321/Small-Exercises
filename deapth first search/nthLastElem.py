# Given a singly linked list l and an integer n, return the value of the nth node from the end of the list. For n=1, return the last node of the list.

# Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    
    curr = l # get head of linked list
    new = [] # empty list
    new.append(curr.value) # add head value
    helper(curr, new) # call helper
    new = new[::-1] # reverse list
    print(new)
    return new[n-1] # return nth element from end
    
    
def helper(curr, new):
    if curr.next: # if there is another element, add it's value to the list
        curr = curr.next
        new.append(curr.value)
        helper(curr, new)


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    
    curr = l # get head of linked list
    new = [] # empty list - Max size of n # [5, 4, 3]
    new.append(curr.value) # add head value
    helper(curr, new, n) # call helper
    return new[0]
    print(new)
    return new[n-1] # return nth element from end
    
    
def helper(curr, new, n):
    if curr.next: # if there is another element, add it's value to the list
        curr = curr.next
        new.append(curr.value)
        if len(new) > n:
            new.pop(0)
        helper(curr, new, n)
    
        
        
# For l = [5, 4, 3] and n = 1, the output should be solution(l, n) = 3;
# For l = [5, 4, 3] and n = 3, the output should be solution(l, n) = 5.
