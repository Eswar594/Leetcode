class Solution:
    def searchRange(self, nums: List[int], k: int) -> List[int]:
        def binarySearch(left):
            l, h = 0, len(nums) - 1
            while l <= h:
                m = (l + h) // 2
                if nums[m] > k or (left and nums[m] == k):
                    h = m - 1
                else:
                    l = m + 1
            return l

        start = binarySearch(True)
        end = binarySearch(False) - 1

        if start <= end < len(nums) and nums[start] == k:
            return [start, end]
        return [-1, -1]
