class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        f_dict = defaultdict(int)
        for num in nums: 
            f_dict[num] +=1 
        sorted_freq = sorted([(value, key) for (key, value) in f_dict.items()], reverse = True )
        result = []
        for i in range(k):
            result.append(sorted_freq[i][1])
        return result


        