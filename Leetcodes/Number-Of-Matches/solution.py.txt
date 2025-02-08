class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        Matches_count = 0
        while n > 1:
            Matches_count += n//2
            if n%2==0:   
                n = n//2
            else:     
                n = n//2 + 1
        return Matches_count 
        # return n-1(shortest solution)