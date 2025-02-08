class Solution:
    def hammingWeight(self, n: int) -> int:
        s = ''
        while n > 0:
            m = n%2
            s = str(m) + s
            n //= 2
        return s.count('1')


        OR 


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res