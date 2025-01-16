class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1 = 0
        for i in nums1:
            xor1 ^= i
        
        xor2 = 0
        for j in nums2:
            xor2 ^= j

        result = 0
        if len(nums1)%2==1:
            result ^= xor2
        if len(nums2)%2==1:
            result ^= xor1

        return result

