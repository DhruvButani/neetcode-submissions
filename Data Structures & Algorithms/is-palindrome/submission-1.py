class Solution:
    def isPalindrome(self, s: str) -> bool:



        string = "".join(c for c in s if c.isalnum() and c != ' ')

        j = len(string)-1
        for i in range(len(string)):

            if(string[i].lower() != string[j].lower()):
                return False
            j-=1
            
        return True
        