class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for a in s: 
            if(a in s_dict):
                s_dict[a]+=1
                continue
            
            s_dict[a] = 1

        for b in t: 
            if(b in t_dict):
                t_dict[b]+=1
                continue
            
            t_dict[b] = 1

        return (s_dict == t_dict)
            