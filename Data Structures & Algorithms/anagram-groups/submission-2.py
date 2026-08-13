from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for str in strs:
            seen["".join(sorted(str))].append(str)
        
        return list(seen.values())