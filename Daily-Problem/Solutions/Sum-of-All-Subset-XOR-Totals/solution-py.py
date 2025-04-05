# Sum of All Subset XOR Totals
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res << len(nums)-1

nums = [5,6,7]
Xor = subsetXORSum(self,nums)
print(Xor)