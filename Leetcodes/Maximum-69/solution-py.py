class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        new_num = ''
        count = 0
        for i in range(len(s)):
            if s[i]=='6' and count == 0:
                new_num += '9'+ s[i+1:]
                count += 1
                break
            else:
                new_num += s[i]
        return int(new_num)
                

        