class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):           #for update the existing element
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break

        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


obj = HashMap()

obj["Aug 16"] = 2004
print(obj.get_hash("Aug 16"))
print(obj.get_hash("Aug 25"))
obj["Aug 25"] = "mathav"
obj["Aug 20"] = 400
print(obj.arr)

print(obj["Aug 20"])