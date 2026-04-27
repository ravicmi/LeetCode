class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import defaultdict 
        if source == target:
            return 0
        level = 0
        stack = [target]
        visited = set()
        visited.add(target)
        new_stack = []
        buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                buses[stop].append(bus_id)
        print(buses)
        while stack: 
            for stop in stack:
                for bus in buses[stop]:
                    for destiny in routes[bus]:
                        if destiny not in visited: 
                            visited.add(destiny)
                            new_stack.append(destiny)
            level +=1 
            if source in visited:
                return level
            stack = new_stack
            new_stack = []
        return -1






        