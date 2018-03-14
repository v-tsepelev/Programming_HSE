class MyHashTable:
    
    def __init__(self, n):
        self.table = [None] * n
        self.size = int(n)

    def char2int(self,char):
        if char >= 'A' and char <= 'Z':
            return ord(char)-65
        elif char >= 'a' and char <= 'z':
            return ord(char)-65-7
        else:
            raise NameError('Invalid character in key! Alphabet is [a-z][A-Z]')       
    
    def hash_function(self, x):
#        if type(x) is str:
#            position = ((len(x)**2) % self.size)
#        if type(x) is int:
#            position = ((x**2) % self.size)
#        return position
        hash = 0
#        for i, c in enumerate (x):
#            hash += pow(52, len(x) - i - 1) * self.char2int(c)
        for i in range(x):
            hash += pow(52, x - i - 1) * x
        return hash % self.size       
    
    def __str__(self):
        output = str(self.table[0]) + " "
        for i in range(1, self.size - 1):
            output += str(self.table[i]) + " "
        output += str(self.table[self.size - 1])
        return output
    
    def add(self, key):
        if None in self.table:
            if self.table[self.hash_function(key)] == None:
                self.table[self.hash_function(key)] = key
                return True
            else:
                return False
        else:
            self.table.append(key)
    
    def delete(self, key):
        if self.table[self.hash_function(key)] == None:
            return False
        else:
            del self.table[self.hash_function(key)]
            return True
    
    def print_sorted(self):
        sorted_table = []
        for i in self.table:
            if i != None:
                sorted_table.append(i)
        sorted_table.sort()
        if not sorted_table:
            return "List is empty!"
        else:
            output = str(sorted_table[0]) + " "
            if len(sorted_table) > 0:
                for i in range(1, len(sorted_table) - 1):
                    output += str(sorted_table[i]) + " "
            if len(sorted_table) > 1:
                output += str(sorted_table[len(sorted_table) - 1])
        return output
    
#table = MyHashTable(7)
#table.add(10)
#table.add(100)
#table.add(3)
#print(table.print_sorted())
#print(table.delete(3), table.delete(33), table.delete(10))
#print(table.print_sorted())
mt = MyHashTable(7)
mt.add(94)
mt.add(13)
mt.add(65)
mt.add(20)
mt.add(42)
mt.add(69)
mt.add(79)
mt.add(76)
mt.add(68)
mt.add(84)
print(mt.print_sorted())


