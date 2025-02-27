 class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        num_set = set(arr)
        max_len = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                pr = arr[j]
                cur = arr[i] + arr[j]
                cur_len = 2

                while cur in num_set:
                    pr, cur = cur, cur + pr
                    cur_len += 1
                    max_len = max(max_len, cur_len)

        return max_len  