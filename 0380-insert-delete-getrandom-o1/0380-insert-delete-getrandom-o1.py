class RandomizedSet:
    from random import choice
    def __init__(self):
        self.value = []
        self.val_to_index = dict()

        

    def insert(self, val: int) -> bool:
        if val not in self.val_to_index:
            self.val_to_index[val] = len(self.value)
            self.value.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            val_index = self.val_to_index[val]
            last_val = self.value[-1]
            self.val_to_index[last_val] = val_index
            self.val_to_index.pop(val)
            self.value[val_index] = last_val
            self.value.pop()
            
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        # print(self.value)
        rand = choice(self.value)
        return rand
        