class Solution:
    def countEven(self, num: int) -> int:
        s,n = 0,num
        while num > 0:
            m = num%10
            s += m
            num//= 10
        if n%2 == 0 and s%2 != 0:
            return n//2 -1
        else:
            return n//2