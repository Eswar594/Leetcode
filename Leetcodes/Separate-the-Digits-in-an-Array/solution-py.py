class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        L = []
        for i in nums:
            for j in str(i):
                L.append(int(j))
        return L