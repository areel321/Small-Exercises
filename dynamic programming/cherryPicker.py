'''
https://leetcode.com/problems/cherry-pickup/solutions/5478591/most-efficient-2-intuitions-explained-wi-3hff
741. Cherry Pickup
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
'''

import math


def cherryPickup(grid: list[list[int]]) -> int:

    """

    Calculates the maximum number of cherries that can be collected 

    by two people starting at (0, 0) and ending at (N-1, N-1).

    This uses a dynamic programming approach where both people take the 

    same number of steps.

    """

    N = len(grid)

    # M is the total number of steps/traversals needed to reach (N-1, N-1)

    # The total number of steps is (N-1) for row + (N-1) for col = 2*N - 2.

    # The loop runs for 0 up to M-1, where M is 2*N - 1.

    M = (N << 1) - 1  # Equivalent to 2 * N - 1

    

    # dp[i][p] stores the maximum number of cherries collected 

    # when the first person is at (i, j) and the second person is at (p, q),

    # where j = n - i and q = n - p.

    # Since j and q depend on the step 'n', we need to update the dp table 

    # for each step 'n'.

    

    # Initialize DP table. Use a large negative number for "unreachable" state, 

    # and 0 for the start.

    dp = [[-1] * N for _ in range(N)]

    dp[0][0] = grid[0][0]

    

    # Iterate through the total number of steps 'n'

    for n in range(1, M):

        # Create a new DP table for the current step 'n'

        new_dp = [[-1] * N for _ in range(N)]

        

        # Iterate over the row indices of the two people: i for person 1, p for person 2

        # We iterate backwards to ensure 'dp' (from step n-1) is used

        # for calculation, not 'new_dp' (which is being built for step n).

        # Note: The Java code reuses 'dp', which requires iterating in a specific order 

        # (inner loops must be backward). To make it clearer and safer, 

        # we'll use a new temporary 'new_dp' table here.

        for i in range(N):

            for p in range(N):

                # Calculate the column indices j and q

                j = n - i

                q = n - p

                

                # --- BOUNDARY AND OBSTACLE CHECK ---

                # Check if the positions (i, j) or (p, q) are out of bounds 

                # or on a thorn (-1).

                if not (0 <= j < N and 0 <= q < N and grid[i][j] != -1 and grid[p][q] != -1):

                    # Unreachable state, remains -1 in new_dp

                    continue

                

                # --- TRANSITION ---

                # current_max_cherries tracks the max cherries collected up to 

                # step n-1, ending at positions that lead to (i, j) and (p, q).

                current_max_cherries = -1

                

                # Person 1 could have come from (i-1, j) or (i, j-1)

                # Person 2 could have come from (p-1, q) or (p, q-1)

                

                # This corresponds to the 4 previous states:

                # 1. P1: (i-1, j), P2: (p-1, q) -> previous DP state: dp[i-1][p-1]

                if i > 0 and p > 0:

                    current_max_cherries = max(current_max_cherries, dp[i - 1][p - 1])

                

                # 2. P1: (i-1, j), P2: (p, q-1) -> previous DP state: dp[i-1][p]

                if i > 0: # and q > 0 is guaranteed by the 'n' step logic

                    current_max_cherries = max(current_max_cherries, dp[i - 1][p])

                

                # 3. P1: (i, j-1), P2: (p-1, q) -> previous DP state: dp[i][p-1]

                if p > 0: # and j > 0 is guaranteed by the 'n' step logic

                    current_max_cherries = max(current_max_cherries, dp[i][p - 1])

                

                # 4. P1: (i, j-1), P2: (p, q-1) -> previous DP state: dp[i][p]

                # This is the state where both people move horizontally 

                # (row index remains the same).

                # The Java code's structure (where only i and p change in the loops) 

                # implicitly covers this as the base case for the current position (i, p) 

                # before the 'max' comparisons.

                # In Python, we explicitly include it:

                current_max_cherries = max(current_max_cherries, dp[i][p])


                # --- UPDATE DP VALUE ---

                if current_max_cherries != -1:

                    # Cherries collected at the current step:

                    cherries = grid[i][j]

                    # Add cherries from the second person's position, 

                    # but only if they are not on the same square (i != p)

                    if i != p:

                        cherries += grid[p][q]

                    

                    new_dp[i][p] = current_max_cherries + cherries

        

        # Update the DP table for the next step

        dp = new_dp


    # The result is the value at the target position (N-1, N-1)

    # The original Java code uses Math.max(dp[N-1][N-1], 0) to handle 

    # the case where the target is unreachable (dp[N-1][N-1] is -1)

    return max(dp[N - 1][N - 1], 0)

class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        memo = [[[-1] * n for _ in range(n)] for _ in range(n)]
        return max(0, self.dp(grid, memo, 0, 0, 0))
    
    def dp(self, grid, memo, r1, c1, c2):
        n = len(grid)
        r2 = r1 + c1 - c2
        
        # Out of bounds or thorn cell
        if r1 >= n or r2 >= n or c1 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')
        
        # Memoization check
        if memo[r1][c1][c2] != -1:
            return memo[r1][c1][c2]
        
        # Base case: reached bottom-right corner
        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        
        # Calculate cherries collected at (r1, c1) and (r2, c2)
        cherries = grid[r1][c1] if r1 == r2 and c1 == c2 else grid[r1][c1] + grid[r2][c2]
        
        # Move right or down
        maxCherries = max(self.dp(grid, memo, r1, c1 + 1, c2), self.dp(grid, memo, r1 + 1, c1, c2))
        # Move down or right
        maxCherries = max(maxCherries, self.dp(grid, memo, r1, c1 + 1, c2 + 1))
        maxCherries = max(maxCherries, self.dp(grid, memo, r1 + 1, c1, c2 + 1))
        
        # Memoize the result
        memo[r1][c1][c2] = maxCherries if maxCherries == float('-inf') else maxCherries + cherries
        
        return memo[r1][c1][c2]


'''
# graph
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        
        cherries = 0

        # right or down
        visited = []
        q = []
        start_point = [0,0]
        point = start_point
        q.append(point)

        while q:
            length = len(q)
            for i in range(0, length):
                point = q.pop(0)
                if grid[point[0]][point[1]] == 1:
                    cherries = cherries + 1
                    grid[point[0]][point[1]] = 0
                visited.append(point)

                # bottom 
                if point[0] < len(grid)-1:
                    bottom = [point[0]+1, point[1]]
                    if bottom not in visited and grid[bottom[0]][bottom[1]] != -1:
                        q.append(bottom)
                
                # right
                if point[1] < len(grid[0])-1:
                    right = [point[0], point[1]+1]
                    if right not in visited and grid[right[0]][right[1]] != -1:
                        q.append(right)

        max_point = [len(grid)-1, len(grid[0])-1]
        if max_point not in visited:
            return 0

        # left or top
        visited = []
        q = []
        point = [len(grid)-1, len(grid[0])-1]
        q.append(point)
        cherries2 = 0

        while q:
            length = len(q)
            for i in range(0, length):
                point = q.pop(0)
                if grid[point[0]][point[1]] == 1:
                    cherries2 = cherries2 + 1
                    grid[point[0]][point[1]] = 0
                visited.append(point)

                # top
                if point[0] > 0:
                    top = [point[0]-1, point[1]]
                    if top not in visited and grid[top[0]][top[1]] != -1:
                        q.append(top)
                # left
                if point[1] > 0:
                    left = [point[0], point[1]-1]
                    if left not in visited and grid[left[0]][left[1]] != -1:
                        q.append(left)

        print(cherries, cherries2, visited)
        if start_point in visited:
            return cherries + cherries2
        else:
            return cherries
'''



