'''
509 fibonacci number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = [0] * (n+1)

        array[0] = 0
        array[1] = 1

        for i in range(2, (n+1)):
            array[i] = array[i-1] + array[i-2]

        return array[n]





'''
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = [0] * (n+1)
        
        return self.helper(array, n)

    def helper(self, array, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        if array[n] > 0:
            return array[n]
        else:
            array[n] = self.helper(array, n-1) + self.helper(array, n-2)
            return array[n]
 '''           


        
