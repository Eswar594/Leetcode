class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = x
        s = 0
        while x > 0:
            m = x%10
            s += m
            x //= 10
        
        if a%s==0:
            return s
        else:
            return -1
        