class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        t = ''
        n = ''
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                t = i + t
        a = 0 
        for j in s:
            if j not in t:
                n += j
            else: 
                n += t[a]
                a += 1
        return n


      OR 


class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1       
        return ''.join(s)

