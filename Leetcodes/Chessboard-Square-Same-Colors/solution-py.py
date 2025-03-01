class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        def color(str):
            value = 0
            for i in str:
                value += ord(i)
            return value

        return (color(coordinate1))%2 == (color(coordinate2))%2
