class MySet:
    def __init__(self,list=[]):
        self.dictionary={}
        for value in list:
            self.dictionary[value] = True

    def __str__(self):
        return f"MySet: {{{','.join(map(str, self.dictionary))}}}"

    def has(self,value):
        return value in self.dictionary

    def add(self,value):
        self.dictionary[value] = True
        return self

    def delete(self,value):
        self.dictionary.pop(value,None)
        return self

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self

st=MySet([1,2,3,4,4])
print(st)