#topics:Hash Table, Linked List
class MyHashSet:

    def __init__(self):
        self.list = dict()
        print("null")
        

    def add(self, key: int) -> None:
        self.list[key] = True
        print("null")
        
        

    def remove(self, key: int) -> None:
        try:
            if self.list[key]:
                self.list[key] =None
        except:
            pass
        print("null")
        
        

    def contains(self, key: int) -> bool:
        try:
            if self.list[key] != None:
                return True
        except:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)