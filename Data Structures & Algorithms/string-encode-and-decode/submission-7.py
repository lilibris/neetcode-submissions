class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return str(strs)
        elif strs == [""]:
            return ""

        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "[]": return s
        return s.split(" ") if len(s)>0 else [s]

        
