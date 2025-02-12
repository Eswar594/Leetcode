class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumOf(n):
            s = 0
            while n>0:
                m = n%10
                s += m
                n = n//10
            return s

        sum_dict = {}
        
        for num in nums:
            s = sumOf(num)
            if s not in sum_dict:
                sum_dict[s] = []
            sum_dict[s].append(num)
        
        max_sum = -1
        
        for key, values in sum_dict.items():
            if len(values) > 1:
                values.sort(reverse=True)
                max_sum = max(max_sum, values[0] + values[1])
        
        return max_sum