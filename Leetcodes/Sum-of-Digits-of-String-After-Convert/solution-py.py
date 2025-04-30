class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def digitSum(n: int,p: int) -> int:
            if p == 0:
                return n
            v = 0
            while n > 0 and p > 0:
                m = n%10
                v += m
                n//= 10
            return digitSum(v,p-1)

        t1 = ''
        for i in s:
            t1 += str(ord(i)-96)
        t1 = int(t1)
        return digitSum(t1,k)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def digitSum(n: int,p: int) -> int:
            if p == 0:
                return n
            v = 0
            while n > 0 and p > 0:
                m = n%10
                v += m
                n//= 10
            return digitSum(v,p-1)

        t1 = ''
        for i in s:
            t1 += str(ord(i)-96)
        t1 = int(t1)
        return digitSum(t1,k)