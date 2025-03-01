class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = 10
        c = 0
        while n >= 0:
            n -= t
            t -= 1
            c += 1

        return c%2 == 0
            
        