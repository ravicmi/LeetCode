class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        start = 0
        end = 1
        def find_longest_palindrome_left_right(l,r):
            while l>=0 and r<N:
                if s[l] != s[r]:
                    break
                l -=1
                r +=1
            return l+1,r
        for i in range(N):
            l,r = find_longest_palindrome_left_right(i,i)
            if r-l > end-start:
                start, end = l, r
            l,r = find_longest_palindrome_left_right(i,i+1)
            if r-l > end-start:
                start, end = l, r

        return s[start:end]

        

        