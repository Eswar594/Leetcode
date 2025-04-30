class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigits(num:int) -> bool:
            dc = 0
            while num:
                dc += 1
                num//=10
            return 1 if dc%2 == 0 else 0

        c = 0
        for num in nums:
            if countDigits(num):
                c += 1
        return c