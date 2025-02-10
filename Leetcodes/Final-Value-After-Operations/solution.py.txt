class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        v = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        return sum(v[i] for i in operations) 