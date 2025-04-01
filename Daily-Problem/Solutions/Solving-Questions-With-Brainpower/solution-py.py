class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        arr = [0] * (n + 1)
        for i in range(n-1,-1,-1):
            pts = questions[i][0]
            bp  = questions[i][1] 
            nxt = i + bp + 1
            sol = 0
            if nxt < n:
                sol += pts + arr[nxt]
            else:
                sol = pts
            skp = arr[i+1]
            arr[i] = max(sol,skp)
        return arr[0]

