class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high = 1, max(candies)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            total_children = sum(candy // mid for candy in candies)

            if total_children >= k:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result