class RandomizedCollection:
    from random import choice
    from collections import defaultdict
    def __init__(self):
        self.value = []
        self.val_to_index = defaultdict(set)
        self.val_counter = defaultdict(int)


    def insert(self, val: int) -> bool:
        self.val_to_index[val].add(len(self.value))
        self.value.append(val)
        self.val_counter[val] +=1
        return self.val_counter[val] ==1

    def remove(self, val: int) -> bool:
        if self.val_counter[val] == 0 :
            return False
        last_val_index = len(self.value)-1
        last_val = self.value[-1]
        val_index  = self.val_to_index[val].pop()
        if val_index != last_val_index:
            self.val_to_index[last_val].remove(last_val_index)
            self.val_to_index[last_val].add(val_index)
        
        self.val_counter[val] -= 1
        self.value[val_index] = last_val
        self.value.pop()
        return True


        

    def getRandom(self) -> int:
        return choice(self.value)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()