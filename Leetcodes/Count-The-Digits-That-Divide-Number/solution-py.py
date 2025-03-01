class Solution:
    def countDigits(self, num: int) -> int:
        num = str(num)
        c = 0
        for i in num:
            if int(num)%int(i) == 0:
                c += 1
        return c
