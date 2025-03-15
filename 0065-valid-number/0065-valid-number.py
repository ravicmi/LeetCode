class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if ('i' in s) or ('n' in s) : 
            return False
        list1 = s.lower().split('e')
        if not len(list1) in (1,2):
            return False
        if len(list1) ==2 : 
            try:
                int(list1[1])
            except:
                return False
        try: 
            float(list1[0])
        except: 
            return False
        
        
        return True
