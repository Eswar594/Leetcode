class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        chairs = 0
        people = 0
        for i in s:
            if i=='E':
                people += 1
                chairs = max(chairs,people)
            else:
                people -= 1
        return chairs

                
