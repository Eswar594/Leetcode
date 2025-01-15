class Solution(object):
    def minimizeXor(self, num1, num2):
        count_set_bits_num2 = bin(num2).count('1')
        x = num1
        
        for i in range(31, -1, -1):
            if (x & (1 << i)) and count_set_bits_num2 > 0:
                count_set_bits_num2 -= 1
            elif (x & (1 << i)):
                x ^= (1 << i)
        
        for i in range(32):
            if count_set_bits_num2 == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                count_set_bits_num2 -= 1
        
        return x
