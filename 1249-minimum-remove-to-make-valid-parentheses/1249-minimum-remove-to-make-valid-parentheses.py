class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = 0 
        r = 0 
        
        for a in s:
            if a == ')':
                r+=1
        output = ''
        for a in s:
            if a == '(':
                if r >0:
                    output +=a
                    l+=1
                    r-=1

                
            elif a == ')':
                if l>0:
                    output +=a
                    l-=1
                else:
                    r -=1
                
            else:
                output +=a
        return output





        