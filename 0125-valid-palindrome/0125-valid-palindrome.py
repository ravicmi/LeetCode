class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        result = True
        left_pointer = 0 
        right_pointer = n-1
        while left_pointer <= n-1 and right_pointer >= 0 : 
            if not s[left_pointer].isalnum():
                left_pointer +=1
            elif not s[right_pointer].isalnum():
                right_pointer -=1
            elif s[right_pointer].lower() != s[left_pointer].lower():
                result = False
                break
            else: 
                left_pointer +=1
                right_pointer -=1
        if (left_pointer != n ):
            if any([a.isalnum() for a in s[left_pointer:]]):
                result = False

        if (right_pointer != -1 ):
            if any([a.isalnum() for a in s[:right_pointer+1]]):
                result = False
        
        return result
            

