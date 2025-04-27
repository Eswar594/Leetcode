class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-2):
            x,y,z = nums[i],nums[i+1],nums[i+2]
            if 2*(x + z) == y:
                c += 1
        return c