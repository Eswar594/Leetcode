class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(haystack) - len(needle)
        for i in range(a+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1