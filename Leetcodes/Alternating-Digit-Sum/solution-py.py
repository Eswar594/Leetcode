class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        for i in range(len(str(n))):
            if i%2 == 0:
                s += int(str(n)[i])
            else:
                s -= int(str(n)[i])
        return s