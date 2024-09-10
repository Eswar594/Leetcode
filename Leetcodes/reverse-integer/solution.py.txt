class Solution(object):
    def reverse(self, x):
        y=x
        if x<0:
            x=-x
        r=0
        while x>0:
            r=(r*10)+x%10
            x//=10
        if y < 0:
            r = -r
        if y >= pow(2,31) or r >= pow(2,31) or y <= pow(-2,31) or r <= pow(-2,31) :
            r = 0
        return r


    
        
        