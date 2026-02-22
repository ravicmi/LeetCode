class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        s = [0,0]
        act = 0
        for index, num in enumerate(nums):
            # print(num%2)
            if (index+1)%6==0:
                act = (act+1)%2
            if num%2==1:
                act = (act+1)%2
            # print(act)
            s[act] += num
            print(s)
        return s[0]-s[1]
                
            
        