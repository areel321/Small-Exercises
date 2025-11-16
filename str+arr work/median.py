# Given a sequence of integers, find its median.

def solution(sequence):
    sequence = sorted(sequence)
    # print(sequence)
    if len(sequence) % 2 == 0: # even
        median_p1 = int(len(sequence) / 2) # middle point right
        median_p2 = median_p1 - 1 # middle point left
        median = (sequence[median_p1] + sequence[median_p2]) / 2 # addition of both middle point values and their avg, the median
        # print(median_p1, median_p2, median)
    else: # odd
        median_point = int(len(sequence) / 2) # get the middle point index
        median = sequence[median_point] # get the middle point value, the median
        # print(median_point, median)
       
    return median
