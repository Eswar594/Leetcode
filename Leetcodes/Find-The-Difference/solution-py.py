class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char_count = {}

        for i in s:
            char_count[i] = char_count.get(i,0) + 1
        
        for j in t:
            char_count[j] = char_count.get(j,0) - 1 
        
        for m,n in char_count.items():
            if n!=0:
                return m
