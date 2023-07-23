class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []
        for w in words:
            w_split = w.split(separator)
            for ws in w_split:
                if ws:
                    ret.append(ws)
        return ret
