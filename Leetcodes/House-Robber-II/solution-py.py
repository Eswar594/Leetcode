class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_case(nums:List[int]) -> int:
            r1,r2 = 0,0
            for i in nums:
                c = max(i+ r1,r2)
                r1 = r2
                r2 = c
            return r2

        if len(nums) == 1:
            return nums[0]

        a = rob_case(nums[:-1])
        b = rob_case(nums[1:])

        return max(a,b)