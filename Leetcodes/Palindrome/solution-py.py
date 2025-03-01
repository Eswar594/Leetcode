class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            num,rev = x,0
            while(num!=0):
                rem = num%10
                rev = rev*10 + rem 
                num//=10
            return x==rev
        