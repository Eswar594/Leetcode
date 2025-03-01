class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sum(nums)
        s = ''
        for i in nums:
            s += str(i)
        
        b = 0
        for i in s:
            b += int(i)
        return abs(a-b)
        