class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char.lower() for char in s if char.isalnum())
        end = len(clean_text) -1
        for start in range(len(clean_text)):
            
            if clean_text[start] == clean_text[end]:
                print(clean_text[start], clean_text[end])
                end -=1
                continue
            elif start == end:
                return True
            else:
                print(clean_text[start], clean_text[end])
                return False
        return True