class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        m = total // cost1
        c = 0
        for i in range(m+1):
            c += (total - cost1*i)//cost2 + 1
        return c