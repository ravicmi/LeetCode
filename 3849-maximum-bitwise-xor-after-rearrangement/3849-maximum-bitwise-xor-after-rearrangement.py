class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        c = [0, 0]
        for d in t: 
            if d == '0':
                c[0] +=1
            else:
                c[1] +=1
        # print(c)
        out = ''
        for ds in s:
            if ds =='0' :
                if c[1]>0:
                    out += '1'
                    c[1] -=1
                else:
                    out += '0'
                    c[0] -=1

            else: 
                if  c[0]>0:
                    out += '1'
                    c[0] -=1
                else:
                    out += '0'
                    c[1] -=1
        return out
                
                
                
            
        