class Solution(object):
    def majorityElement(self, nums):
        num_freq = {}
        for i in nums:
            if i in num_freq:
                num_freq[i] += 1
            else:
                num_freq[i] = 1 
        
        return max(num_freq,key=num_freq.get)

        