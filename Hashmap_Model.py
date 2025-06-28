class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


obj = HashMap()
print(obj.arr)

obj["Aug 16"] = 2004
obj["sep 16"] = "mathav"
obj["jan"] = 54
obj['mar 4'] = [40,5,2]
obj['mar 12'] = 2
obj['mar 10'] = 5
# obj['mar 20'] = 10

print(obj.get_hash("Aug 16"))
print(obj.arr)

print(obj.get_hash("Aug"))
print(obj.get_hash("aug"))

print(obj.arr[0])



# but in normal hashmap collision occur so we move to linear probing or seperate chaining