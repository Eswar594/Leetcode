class Solution(object):
    def toLowerCase(self, s):
        lower_str = ''
        for i in s:
            if i.isalpha() and ord(i) < 97:
                lower_str += chr(ord(i)+32)
            else:
                lower_str += i
        return lower_str
        