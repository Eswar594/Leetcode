class Solution:
    def reverseDegree(self, s: str) -> int:
        rd = 0
        for i in range(len(s)):
            rd += (123 - ord(s[i])) * (i+1)
        return rd
