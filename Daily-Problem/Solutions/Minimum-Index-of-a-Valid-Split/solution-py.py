class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        fm = defaultdict(int)
        sm = defaultdict(int)
        n = len(nums)

        for num in nums:
            sm[num] += 1
        for idx in range(n):
            num = nums[idx]
            sm[num] -= 1
            fm[num] += 1

            if(fm[num]*2 > idx+1 and sm[num]*2 > n-idx-1):
                return idx

        return -1


