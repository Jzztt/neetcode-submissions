class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] +=1
            else:
                s_dict[i] = 1
        for y in t:
            if y in t_dict:
                t_dict[y] +=1
            else:
                t_dict[y] = 1
        if s_dict == t_dict:
            return True
        else:
            return False
            
        
            
            
                
                