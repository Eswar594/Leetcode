class Solution(object):
    def canConstruct(self, s, k):

        char_count = {}
        odd_count = 0

        for i in s:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        

        for i in char_count.values():
            if i%2!=0:
                odd_count+=1

        if len(s) < k or odd_count > k :
            return False
        else:
            return True
            
        