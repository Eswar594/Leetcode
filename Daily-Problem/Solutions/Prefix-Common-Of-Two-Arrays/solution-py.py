class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        common = []
        for i in range(1,len(A)+1):
            count = 0
            for j in range(i):
                if B[j] in A[0:i]:
                    count += 1 
            common.append(count)
        return common
        