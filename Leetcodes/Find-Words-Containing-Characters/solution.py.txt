class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        List = []
        for i in range(len(words)):
            if x in words[i]:
                List.append(i)
        return List