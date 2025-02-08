class Solution(object):
    def waysToSplitArray(self, nums):
        nums_sum = sum(nums)
        left_nums_sum = 0
        count = 0
        for i in range(len(nums)-1):
            left_nums_sum += nums[i]
            right_nums_sum = nums_sum - left_nums_sum
            if left_nums_sum >= right_nums_sum:
                count += 1
        return count 

        