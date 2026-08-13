from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn =[]
        seen=defaultdict(list)
        # group by length then check anagram 
        for str in strs:
            for key in seen:
                if len(key) == len(str) and sorted(key) == sorted(str):
                    seen[key].append(str)
                    break
            else:
                seen[str].append(str)
            #print(seen)
        for key in seen:
            rtn.append(seen[key])
        return rtn
