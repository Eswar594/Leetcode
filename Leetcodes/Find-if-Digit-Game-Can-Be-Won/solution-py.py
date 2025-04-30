class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1 = s2 = 0
        for i in nums:
            if i%10 == i:
                s1 += i
            else:
                s2 += i
        return s1 != s2