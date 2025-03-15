class Solution:
    def minCapability(self, nums, k):
        l, r = 1, max(nums)
        n = len(nums)

        while l < r:
            m = (l + r) // 2
            p = 0
            i = 0
            while i < n:
                if nums[i] <= m:
                    p += 1
                    i += 2
                else:
                    i += 1
            if p >= k:
                r = m
            else:
                l = m + 1

        return l
