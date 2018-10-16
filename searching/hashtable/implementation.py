class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] *self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:
                next_slot = self.rehash(hashvalue, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                else:
                    self.data[next_slot] = data

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop, found = False, False
        position = startslot

        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldslot, size):
        return (oldslot + 1) % size


h = HashTable(5)
h[1] = "a"
h[2] = "b"
h[2] = "c"
h[10] = "cc"

print(h[10])