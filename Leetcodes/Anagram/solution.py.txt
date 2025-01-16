class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_char = {}
        for i in s:
            count_char[i] = count_char.get(i,0)+1
        
        for j in t:
            count_char[j] = count_char.get(j,0)-1
        
        for k in count_char.values():
            if k!=0:
                return False
            
            
        return True