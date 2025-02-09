class Solution:
    def is_palindrome(self, s:str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False
    def longestPalindrome(self, s: str) -> str:
        max_pal = 0
        required_str = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j+1]):
                    new_max_pal =  (j-i+1)
                    if new_max_pal >= max_pal:
                        max_pal = new_max_pal
                        required_str = s[i:j+1]
        return required_str

        