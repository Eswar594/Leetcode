class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)


        for i in range(len(nums)):
            if target < nums[i]:
                return i 
        else:
            return len(nums)


        