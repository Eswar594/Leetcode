class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,ch in enumerate(s):
            last[ch] = i

        res = []
        st = 0
        end = 0

        for i,ch in enumerate(s):
            end = max(end,last[ch])
            if i==end:
                res.append(end-st+1)
                st = i+1
        return res