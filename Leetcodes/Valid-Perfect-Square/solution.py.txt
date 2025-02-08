class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(1, int(num**0.5) + 1):
            if i ** 2 == num:
                return True
       
        return False
        