	class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(sorted(nums))
        if(max(nums)<=0):
            return 1
        for i in range(1,max(nums)+100):
            if i not in nums:
                return i