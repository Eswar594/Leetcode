class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        odd,even = 0,0
        for i in nums:
            if i>0:
                even += 1
            elif i<0:
                odd += 1
        return max(odd,even)
