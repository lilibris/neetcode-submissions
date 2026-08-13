from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s.lower())
        t_count = Counter(t.lower())
        if len(s_count) >= len(t_count):
            for k, v in s_count.items():
                if k not in t_count or v != t_count[k]:
                    return False
            else:
                return True
        else:
            for k, v in t_count.items():
                if k not in s_count or v != s_count[k]:
                    return False
            else:
                return False