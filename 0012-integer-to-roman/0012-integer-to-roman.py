class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {1: 'I', 5:'V', 10:'X', 50:'L', 100: 'C', 500:'D', 1000:'M'}
        roman = ''
        a = num//1000
        if a:
            roman += 'M'*a

        num = num%1000
        a = num//100
        if a==9:
            roman += 'CM'
        else:
            if a>=5:
                a = a-5 
                roman += 'D'
            if a == 4:
                roman += 'CD'
            else: 
                roman += a*'C'

        num = num%100
        a = num//10
        if a==9:
            roman += 'XC'
        else:
            if a>=5:
                a = a-5 
                roman += 'L'
            if a == 4:
                roman += 'XL'
            else: 
                roman += a*'X'
        
        num = num%10
        a = num
        if a==9:
            roman += 'IX'
        else:
            if a>=5:
                a = a-5 
                roman += 'V'
            if a == 4:
                roman += 'IV'
            else: 
                roman += a*'I'
        return roman

            
        



        