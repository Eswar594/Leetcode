class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = 0
        while (n>0):
            m = n % k
            s += m
            n //= k
        return s