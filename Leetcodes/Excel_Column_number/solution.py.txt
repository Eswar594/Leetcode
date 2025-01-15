class Solution(object):
    def titleToNumber(self, columnTitle):
        column_num = 0
        for i in columnTitle:
            column_num = 26*column_num + ord(i)-64 
        return column_num
            

        