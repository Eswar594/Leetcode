class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        comp_freq = defaultdict(int)

        for v in range(n):
            g[v] = [v]

        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)

        for v in range(n):
            ngbs = tuple(sorted(g[v]))
            comp_freq[ngbs] += 1

        return sum(1 for ngbs,freq in comp_freq.items() if len(ngbs)==freq )
