class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        List = []
        for i in range(1,n+1):
            if n%i==0:
                List.append(i)
        if len(List) < k:
            return -1
        else:
            return List[k-1]

        