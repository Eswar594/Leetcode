class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        i = even = odd = 0
        while n > 0:
            m = n%2
            if m == 1:
                if i%2 == 0:
                    even += 1
                else:
                    odd += 1
            i += 1
            n//= 2
        return [even,odd]