class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = [int(a) for a in num1]
        l2 = [int(a) for a in num2]
        carry = 0
        out = []
        while l1 and l2 :
            d1 = l1.pop()
            d2 = l2.pop()
            c = d1+d2+carry
            out.append(c%10)
            carry = c//10
        
        while l1  :
            d1 = l1.pop()
            c = d1+carry
            out.append(c%10)
            carry = c//10
        while l2  :
            d1 = l2.pop()
            c = d1+carry
            out.append(c%10)
            carry = c//10
        if carry > 0:
            out.append(carry)

        result =  ''.join([str(a) for a in out[::-1]])
        return result



