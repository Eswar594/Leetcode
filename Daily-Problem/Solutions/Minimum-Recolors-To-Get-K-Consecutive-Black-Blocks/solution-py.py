class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        w = 0
        c = float("inf")

        for r in range(len(blocks)):
            if blocks[r] == "W":
                w += 1
            if r-l + 1 ==k:
                c = min(c,w)
                if blocks[l] == "W":
                    w -= 1
                l += 1 
        return c 