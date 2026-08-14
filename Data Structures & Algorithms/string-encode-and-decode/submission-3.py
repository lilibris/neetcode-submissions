class Solution:

    def encode(self, strs: List[str]) -> str:
        #print(" ".join(strs))
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        #print(s.split())
        
        return s.split(" ") if len(s)>0 else [""]
