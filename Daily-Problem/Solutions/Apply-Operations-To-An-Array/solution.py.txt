class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        List = []
        c = 0
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1] and nums[i]!=0:
                nums[i] *= 2
                nums[i+1] = 0
        
        for i in nums:
            if i!= 0:
                List.append(i)

        for j in range(len(nums)-len(List)):
            List.append(0)

        return List

        