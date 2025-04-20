class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = 0
        answers.sort()
        while len(answers) > 0:
            t = answers[0]
            sc = t + 1
            s += sc
            while sc > 0 and t in answers:
                answers.remove(t)
                sc -= 1
        return s