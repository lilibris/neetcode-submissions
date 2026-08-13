class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn=defaultdict(list)
        for str in strs:
            count=[0]*26
            for c in str:
                count[ord(c)-ord('a')] +=1
            rtn[tuple(count)].append(str)
        return list(rtn.values())