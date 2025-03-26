class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for r in grid for num in r]
        m = nums[0] % x

        if any(num % x != m for num in nums):
            return -1

        nums.sort()
        med = nums[len(nums)//2]
        return sum(abs(num-med)// x for num in nums)