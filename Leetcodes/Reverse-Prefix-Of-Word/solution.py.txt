class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = word.find(ch)
        a = word[0:n+1]
        return a[::-1] + word[n+1:]
        