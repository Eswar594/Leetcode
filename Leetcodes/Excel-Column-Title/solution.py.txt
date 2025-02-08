class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        columnTitle = ''
        while columnNumber > 0:
            columnNumber -= 1
            columnTitle = chr((columnNumber % 26) + 65) + columnTitle
            columnNumber //= 26 
        return columnTitle