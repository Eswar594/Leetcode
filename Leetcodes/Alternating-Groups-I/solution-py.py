class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors += colors[0:2]
        c = 0
        for i in range(1,len(colors)-1):
            if colors[i]!=colors[i-1] and colors[i]!=colors[i+1]:
                c += 1
        return c