
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        letterMap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        #create a frequency array
        bucket  = 0
        mydict = {}
        for item in strs:
            codedArray = [0 for i in range(26)]
            for letter in item:
                codedArray[letterMap[letter]] +=1
            codedMap = '-'.join(map(str, codedArray))
            print(codedMap)
            if codedMap in mydict:
                mydict[codedMap].append(item)
            else:
                mydict[codedMap] = [item]

        sol = []
        for key in mydict:
            sol.append(mydict[key])

        return sol