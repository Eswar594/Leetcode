1. Method-1
class Solution:
    def clearDigits(self, s: str) -> str:
        t = ""
        for i in s:
            if i.isdigit() and len(t)!=0:
                t = t[:len(t)-1]
            else:
                t += i
        return t 

2.Method-2

class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and i.isdigit():
                stack.pop(-1)
            else:
                stack.append(i)
        return "".join(stack)
        
        