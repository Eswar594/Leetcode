class Solution(object):
    def singleNumber(self, nums):
        num_freq = {}
        for i in nums:
            if i in num_freq:
                num_freq[i] += 1
            else:
                num_freq[i] = 1

        for i,j in num_freq.items():
            if j==1:
                return i

        