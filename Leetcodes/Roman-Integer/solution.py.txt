class Solution(object):
    def romanToInt(self, s):
        Char_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val = 0
        for i in range(len(s)-1):
            if Char_val[s[i]] < Char_val[s[i+1]]:
                val -= Char_val[s[i]]
            else:
                val +=Char_val[s[i]]
        val += Char_val[s[-1]]
        
        return val 