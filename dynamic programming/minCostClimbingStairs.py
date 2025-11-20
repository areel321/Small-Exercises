'''
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=problem-list-v2&envId=dynamic-programming
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # of next two steps, take the lesser one
        # if equal, take two steps
        

        array = [0] * (len(cost)) # array to hold cost at each step

        array[0] = cost[0] # 0th step is 0 cost
        array[1] = cost[1] # 1st step is 1 cost

        for i in range(2, len(cost)):
            # minimum to reach that level
            array[i] = cost[i] + min(array[i-1], array[i-2])

        # cost at final step
        print(array)
        return min(array[len(cost)-1], array[len(cost)-2])
