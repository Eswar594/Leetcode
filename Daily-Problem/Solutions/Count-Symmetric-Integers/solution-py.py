class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low,high+1):
            a = str(i)
            if len(a)%2==0:
                n = len(a)//2
                if sum([int(m) for m in a[:n]])==sum([int(n) for n in a[n:]]):
                    c += 1
        return c