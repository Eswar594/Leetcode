class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}
        for i in range(1,n+1):
            s = 0
            while i > 0:
                m = i%10
                s += m
                i //= 10
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
        g = list(freq.values())
        return g.count(max(g))
