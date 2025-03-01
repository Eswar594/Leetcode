class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        t = [0]*len(indices)
        for i in range(len(s)):
            t[indices[i]] = s[i]
        return ''.join(t)
        

        