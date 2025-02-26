class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum,minsum,presum = 0,0,0

        for i in nums:
            presum += i 
            minsum = min(presum,minsum)
            maxsum = max(presum,maxsum)

        return maxsum - minsum 
     

        
        