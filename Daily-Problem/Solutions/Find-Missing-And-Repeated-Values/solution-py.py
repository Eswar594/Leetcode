class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        List = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a = grid[i][j]
                List.append(a)

        n = len(List)
        s = int(n * (n+1) * 0.5)
        mr = []
        for i in List:
            if List.count(i)==2:
                mr.append(i)
                break
        a = (s + mr[0]) - sum(List)
        mr.append(a)
        return mr
        return List