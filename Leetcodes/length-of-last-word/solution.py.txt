class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        l=s.split(" ")
        return len(l[-1])

        