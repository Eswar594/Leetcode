class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = bin(num)[2:]
        s = ''
        for i in a:
            if i=='1':
                s += '0'
            else:
                s += '1'
        return int(s,2)
        