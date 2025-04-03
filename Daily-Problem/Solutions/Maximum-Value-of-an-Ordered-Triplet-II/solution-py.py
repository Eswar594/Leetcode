class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        lm = [0]*n
        rm = [0]*n
        for i in range(1,n):
            lm[i] = max(lm[i-1],nums[i-1])
            rm[n-i-1] = max(rm[n-i],nums[n-i])
        res = 0
        for j in range(1,n-1):
            res = max(res,(lm[j]-nums[j])*rm[j])
        return res
