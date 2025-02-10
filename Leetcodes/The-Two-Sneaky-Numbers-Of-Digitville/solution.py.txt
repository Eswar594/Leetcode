class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        List = []
        for i in set(nums):
            if nums.count(i) == 2:
                List.append(i)
        return List