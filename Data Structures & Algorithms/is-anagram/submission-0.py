class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = tuple(s)
        s = sorted(s)
    
        t = tuple(t)
        t = sorted(t)
        
        if s == t:
            return True
        else:
            return False
        