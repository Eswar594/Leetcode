class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            s = 0
            while num > 0:
                m = num%10
                s += m
                num//= 10
            num = s
        return num