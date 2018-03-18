class MyHashTable:
    
    def __init__(self, n):
        self.size = int(n)
        self.table = [[] for i in range(self.size)]        

    def char2int(self,char):
        if char >= 'A' and char <= 'Z':
            return ord(char)-65
        elif char >= 'a' and char <= 'z':
            return ord(char)-65-7
        else:
            raise NameError('Invalid character in key! Alphabet is [a-z][A-Z]')       
    
    def hash_function(self, x):
        hash = 0
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
        if key not in self.table[self.hash_function(key)]:
            self.table[self.hash_function(key)].append(key)
            return True
        else:
            return False
    
    def delete(self, key):
        if key not in self.table[self.hash_function(key)]:
            return False
        else:
            del self.table[self.hash_function(key)][self.table[self.hash_function(key)].index(key)]
            return True
    
    def print_sorted(self):
        sorted_table = []
        for i in self.table:
            for j in i:
                sorted_table.append(j)
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
