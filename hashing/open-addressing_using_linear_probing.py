class open_Adreesing:
    def __init__(self , capacaity,size):
        self.capacity = capacaity
        self.table = [-1]*capacaity
        self.size = 0

    def hash_value(self,key):
        return key%self.capacity
    def search(self , key):
        H = self.hash_value(key)
        T = self.table
        i = H
        while T[H] != -1:
            if T[i] == key:
                return True
            i = (i+1)%self.capacity
            if i == H:
                return False
        return False

    def remove(self,key):
        H = self.hash_value(key)
        T = self.table
        i = H
        while T[i] != -1:
            if T[i] == key:
                self.T[i] = -2
            i = (i+1)%self.capacity
            if i == H:
                return False
        return False
    def insert(self,key):
        if self.capacity == self.size:
            return False
        if self.search(key) == True:
            return False
        h = self.hash_value(key)
        t = self.table
        i = h
        while t[i] not in (-1,-2):
            i = (i+1)%self.capacity
        t[i] = key
        self.size +=1
        return True

        
        

