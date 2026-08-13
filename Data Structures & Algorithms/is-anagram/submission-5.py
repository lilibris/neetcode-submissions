from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s.lower())
        t_count = Counter(t.lower())
        for k, v in s_count.items():
            if k not in t_count or t_count[k] != v:
                return False 
        else:
            return True