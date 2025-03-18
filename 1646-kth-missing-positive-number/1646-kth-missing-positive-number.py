class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = 0
        count = 0
        index = 0 
        curr = arr[index]
        while count < k : 
            m +=1
            if curr == m: 
                if index < len(arr)-1:
                    index +=1 
                    curr = arr[index]
                    
            else:                     
                count +=1 
                
        return m




        