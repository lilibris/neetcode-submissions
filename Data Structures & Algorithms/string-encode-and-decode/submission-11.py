class Solution:

    def encode(self, strs: List[str]) -> str:
        # length@ as dlimeter
        if not strs or strs == [""]: # [] or [""]
            return str(strs)
        rtn = "".join(f"{len(word)}@{word}" for word in strs)
        print(rtn)
        return rtn

    def decode(self, s: str) -> List[str]:
        if s == "[]":
             return []
        elif s == "['']":
             return [""]
        rtn, i = [], 0
        while i < len(s):
            right = i
            # find the delimiter first:
            while s[right] != "@":
                right += 1
            word_len = int(s[i:right])
            rtn.append(s[right+1:right+1+word_len])
            i = right+1+word_len
        return rtn



        
