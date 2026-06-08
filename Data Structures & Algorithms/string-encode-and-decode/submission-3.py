class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

     
        for s in strs:
            encodedString += str(len(s)) + "#" + s

        return encodedString

    def decode(self, s: str) -> List[str]:
        solString = []

        i = 0

        while(i<len(s)):
            count = ''
            while(s[i] != '#'):
                count += s[i]
                i+=1
            count = int(count)
            i+=1

            solString.extend([s[i:i+count]])
            i+=count

        return solString
