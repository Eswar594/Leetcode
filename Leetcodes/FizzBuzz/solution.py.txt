class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        Array = []
        for i in range(1,n+1):
            if i%15==0:
                Array.append("FizzBuzz")
            elif i%5 == 0:
                Array.append("Buzz")
            elif i%3 == 0:
                Array.append("Fizz")
            else:
                Array.append(str(i))
        return Array
