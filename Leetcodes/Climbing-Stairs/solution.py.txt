class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        p1=1
        p2=2
        c=0
        for i in range(3,n+1):
            c=p1+p2
            p1=p2
            p2=c
        return c
        
        