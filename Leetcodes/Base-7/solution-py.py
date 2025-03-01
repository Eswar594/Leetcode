class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        s = ''
        a = num
        num = abs(num)
        while num!=0:
            m = num%7
            s = str(m) + s
            num //=7
        if a < 0:
            s = '-' + s
        return s

