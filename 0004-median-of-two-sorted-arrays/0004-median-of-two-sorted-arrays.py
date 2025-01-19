class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        def median(sort_list):
            l = len(sort_list)
            if l%2:
                return sort_list[l//2]
            else: 
                return (sort_list[(l-1)//2] + sort_list[l//2])/2
        print(num1)
        print(num2)
        l1 = len(num1)
        l2 = len(num2)
        if l1==0:
            return median(num2)
        if l2==0:
            return median(num1)
        if l1 <=2 and l2 <=2:
            new_num = sorted(num1+num2)
            return median(new_num)
        if l1 <=2:
            print(num1)
            print(num2[(l2-1)//2-1 : (l2//2)+1])
            new_num = sorted(num1+num2[(l2-1)//2-1 : (l2//2)+2])
            return median(new_num)
        if l2 <=2:
            new_num = sorted(num2+num1[(l1-1)//2-1 : (l1//2)+2])
            return median(new_num)
        m1 = median(num1)
        m2 = median(num2)
        l_min = (min(l1, l2)-1)//2
        
        if m1 <=m2:
            result_med =  self.findMedianSortedArrays(num1[l_min:], num2[:-l_min])
            return result_med
        else: 
            result_med =  self.findMedianSortedArrays(num2[l_min:], num1[:-l_min])
            return result_med
        