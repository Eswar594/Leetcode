class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in sentences:
            a = len(i.split(" "))
            if a > max: max = a
        return max
