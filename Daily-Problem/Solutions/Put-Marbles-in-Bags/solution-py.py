class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        weights = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
        weights.sort()
        ans = 0
        for i in range(k-1):
            ans += weights[len(weights)-1-i] - weights[i]
        return ans