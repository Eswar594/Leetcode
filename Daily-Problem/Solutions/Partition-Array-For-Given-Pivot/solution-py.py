class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = nums.count(pivot)
        l = []
        r = [] 
        print(a)
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i > pivot:
                r.append(i)
        return l + a*[pivot] + r


