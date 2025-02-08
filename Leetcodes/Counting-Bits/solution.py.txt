class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        count = []
        s = ''
        for i in range(n+1):
            s = bin(i)[2:]
            a = s.count('1')
            count.append(a)
        return count



        