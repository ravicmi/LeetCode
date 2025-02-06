class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        glo_max = 0 
        if len(points) <3 : 
            return len(points)
        num_points = len(points)
        for i, point_i in enumerate(points[:-2]):
            x1, y1 = point_i
            for j, point_j in enumerate(points[i+1:-1]):
                if point_j != point_i:
                    x2, y2 = point_j
                    curr_max = 2
                    print('for. ', point_i, point_j)
                    if x1 != x2:
                        slope = (y2-y1)/(x2-x1)
                    for k, point_k in enumerate(points[i+j+1:]):
                        if (point_j == point_i) or (point_j == point_k):
                            continue
                        x3, y3 = point_k
                        if x1 != x2: 
                            if x2 != x3:
                                if slope == (y2-y3)/(x2-x3):
                                    curr_max +=1
                                    print(x3, y3)
                        else: 
                            if x2 == x3:
                                curr_max +=1 
                                print(x3, y3)
                        glo_max = max(glo_max, curr_max)
        return glo_max

