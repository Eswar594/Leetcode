class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if nums.count(nums[i]) > 1:
                nums.remove(nums[i])
            else:
                i += 1
