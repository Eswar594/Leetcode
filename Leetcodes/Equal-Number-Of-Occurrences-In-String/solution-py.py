class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_freq = {}
        for i in s:
            char_freq[i] = char_freq.get(i,0) + 1
        
        a  = char_freq[s[0]]
        for i in char_freq.values():
            if a!=i:
                return False
        return True
