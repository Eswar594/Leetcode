class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        num = 0
        for i in coordinates:
            num += ord(i)
        return num%2==1
            