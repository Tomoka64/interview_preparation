import ctypes

class DynamicArray(object):
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.array = self.makeArray(self.capacity)
    
    def __len__(self):
        return self.length
    
    def __getItem__(self, i):
        if not 0 <= i < self.length:
            return IndexError("index out of range")
        return self.array[i]

    def append(self, element):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = element
        self.length += 1
    
    def _resize(self, new_cap):
        resized = self.makeArray(new_cap)
        for i in range(self.length):
            resized[i] = self.array[i]
        
        self.array = resized
        self.capacity = new_cap
    
    def makeArray(self, cap):
        return (cap * ctypes.py_object)()
    
arr = DynamicArray()
arr.append(1)
arr.append(1)
print(len(arr))