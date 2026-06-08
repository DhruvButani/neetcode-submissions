class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counterDict = {}

        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in counterDict:
                counterDict[sortedStr].append(s)
            else:
                counterDict[sortedStr] = [s]

        return [v for v in counterDict.values()]
        