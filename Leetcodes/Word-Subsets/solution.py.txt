class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        List = [[]]
        for num in nums:
            List += [current + [num] for current in List]
        return List
               


            
        