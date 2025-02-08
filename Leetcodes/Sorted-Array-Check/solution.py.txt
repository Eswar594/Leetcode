class Solution:
    def check(self, nums: List[int]) -> bool:
        List = []
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                List = nums[i+1:] + nums[0:i+1]
        print(List)
        return List == sorted(List)

        