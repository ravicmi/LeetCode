class Solution:
    from collections import Counter, defaultdict
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = {0:1}
        a = 1 
        for i in range(1, 10):
            a *=i
            fact[i] = a
        
        # org_list = [a for a in str(n)]
        # org_dict = Counter(org_list)
        org_dict = defaultdict(int)
        new_dict = defaultdict(int)
        dig_n = 0
        while n: 
            dig_n += fact[n%10]
            org_dict[n%10] +=1
            n = n//10
        # print(dig_n)
        while dig_n:
            new_dict[dig_n%10] +=1
            dig_n = dig_n//10
        # new_dict = Counter([a for a in str(dig_n)])
        result = True 
        for i in range(10):
            if new_dict[i] != org_dict[i]:
                result = False
        # print(fact)
        # print(org_dict)
        
        # print(new_dict)
        return result
        
        