class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        comp = set()
        while n!=1:
            if n in comp:
                return False
            comp.add(n)
            s = 0
            while n > 0:
                m = n%10 
                s += m * m
                n //= 10
            n = s

        return True 

            
        