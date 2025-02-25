class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        m = 1e9 + 7
        n = len(arr)
        c = 0

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s % 2 != 0:
                    c += 1

        return int(c % m)