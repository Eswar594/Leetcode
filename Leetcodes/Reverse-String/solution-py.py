class Solution(object):
    def reverseString(self, s):
        l = s[0]
        r = s[-1]
        for i in range(len(s)//2):
            s[i] = r
            s[len(s)-i-1] = l
            l = s[i+1]
            r = s[len(s)-i-2]
        return s 
        
             OR

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l= 0
        r = len(s)-1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return s
