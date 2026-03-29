class EventManager:
    import heapq
    from collections import defaultdict

    def __init__(self, events: list[list[int]]):
        self.hp = []
        self.priority = dict()
        for event in events:
            heapq.heappush(self.hp, (-event[1], event[0]))
            self.priority[event[0]] = -event[1]
        self.stale = defaultdict(int)
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        heapq.heappush(self.hp, (-newPriority, eventId))
        oldPriority = self.priority[eventId]
        self.priority[eventId] = -newPriority
        self.stale[(oldPriority, eventId)] +=1
        # print(self.hp)
        # print(self.stale)
        
        

    def pollHighest(self) -> int:
        if not self.hp: 
            return -1
        while self.hp:
            event = heapq.heappop(self.hp)
            if self.stale[event] ==0:
                return event[1]
            else:
                self.stale[event] -=1
        return -1

            
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()