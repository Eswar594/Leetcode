class Solution(object):
    def minimumLength(self, s):
        min_len = 0
        a = set(s)
        for i in a:
            if s.count(i)%2==0:
                min_len += 2
            else:
                min_len += 1

        return min_len
