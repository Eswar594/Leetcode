class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num//3
        if a == num/3:
            return [a-1,a,a+1]
        else:
            return []