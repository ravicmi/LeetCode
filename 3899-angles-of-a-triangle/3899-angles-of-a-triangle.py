class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        import math
        mx = max(sides)
        sum_of_2 = sum(sides)-mx
        if (mx >= sum_of_2): 
            return []
        out = []
        sides.sort()
        a, b, c = sides
        lst = [(a,b,c), (b,c, a), (c,a, b)]
        for pr in lst: 
            x, y, z = pr
            var = (x*x + y*y - z*z)/(2*x*y)
            angle = math.acos(var)
            out.append(math.degrees(angle))
        out.sort()
        return out
        