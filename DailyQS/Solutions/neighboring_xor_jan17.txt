class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        x = 0
        for i in derived:
            x ^= i
        return x==0
        
        


