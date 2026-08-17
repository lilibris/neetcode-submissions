class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s) -1
        for start in range(len(s.strip())):
            if not s[start].isalnum() or not s[end].isalnum():
                continue
            if s[start].lower() == s[end].lower():
                end -=1
                continue
            elif start == end:
                return True
            else:
                print(s[start], s[end])
                return False
        return True