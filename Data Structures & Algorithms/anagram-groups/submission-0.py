class Solution:
    def groupAnagrams(self, x: List[str]) -> List[List[str]]:
        y = {}
        for i in x:
            l = "".join(sorted(i))
            if l not in y:
                y[l] = []
            y[l].append(i)

        return list(y.values())
