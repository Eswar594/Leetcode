class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        selected = [False] * len(tiles)

        self.gen_seq(tiles,"",selected,seq)
        return len(seq)-1

    def gen_seq(self,tiles:str,current:str,selected:list,seq:set)->None:
        seq.add(current)

        for pos,ch in enumerate(tiles):
            if not selected[pos]:
                selected[pos] = True
                self.gen_seq(tiles,current + ch,selected,seq)
                selected[pos] = False