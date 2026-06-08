class Solution:
    def isValid(self, s: str) -> bool:
        s = s.replace("()","")
        s = s.replace("[]","")
        s = s.replace("{{}}".format(),"")
        
        if(len(s) == 0):
            return True

        openingSequence = {"{":3,"(":2,"[":1}
        closingSequence = {"}":3,")":2,"]":1}
        sequence = []
        for x in s:
            if(x in openingSequence):
                sequence.append(openingSequence[x])
            else:
                
                if(len(sequence) == 0 or closingSequence[x] != sequence[len(sequence)-1]):
                    return False
                sequence = sequence[:-1]
    
        
        if(len(sequence) !=0):
            return False

        return True
        