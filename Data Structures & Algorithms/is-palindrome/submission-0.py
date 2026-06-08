class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for c in s:
            if c.isalnum():
                l.append(c.lower())

        mid = int(len(l)/2)
        if(len(l)%2==1):
            mid+=1
        
        for i in range(mid):
            if(l[len(l)-1-i] != l[i]):
                return False

        return True
        