class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = 0
        for i in nums:
            if i > 9:
                a += i
            else:
                a -= i 
        return a!=0
        