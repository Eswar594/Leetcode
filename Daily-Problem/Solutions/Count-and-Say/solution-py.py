class Solution:
    def countAndSay(self, n: int) -> str:
        def countStr(s:str) -> str:
            c = 1
            a = ''
            for i in range(1,len(s)):
                if s[i-1] == s[i]:
                    c += 1
                else:
                    a += str(c) + s[i-1]
                    c = 1
            a += str(c) + s[-1]
            return a

        base = "1"
        for k in range(n-1):
            base = countStr(base)
        return base



