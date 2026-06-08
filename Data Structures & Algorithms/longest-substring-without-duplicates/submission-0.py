class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streak = 0
        window = set()
        left = 0

        for c in s:
            initial = len(window)
            window.add(c)

            if(initial == len(window)):
                removedChar = s[left]
                window.discard(s[left])
                left+=1
            
                while(removedChar != c):
                    removedChar = s[left]
                    window.discard(s[left])
                    left+=1

                window.add(c)
                
            if len(window)>streak:
                streak = len(window)
        
        return streak
        