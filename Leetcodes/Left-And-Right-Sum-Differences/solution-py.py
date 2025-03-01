class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        List = []
        l = 0
        r = sum(nums)
        for i in nums:
            l += i
            List.append(abs(l-r))
            r -= i
        return List


        