class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1]
        r = 0
        c = 1 
        for i in range(1,len(colors)):
            if colors[i-1] != colors[i]:
                c += 1
            else:
                c = 1
            if c >= k:
                r += 1
        return r
               
