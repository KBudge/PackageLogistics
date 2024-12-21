
# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all indexes with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty index list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts new Info into the hash table.
    def insert(self, ID, Info): # does both insert and update
        # get the index list where this Info will go.
        index = hash(ID) % len(self.table)
        index_list = self.table[index]

        # update Info if ID is already in the index
        for k in index_list:
            #print (Info)
            if k[0] == ID:
                k[1] = Info
                return True

        # if not, insert the Info to the end of the index list.
        key_value = [ID, Info]
        index_list.append(key_value)
        return True

    # Searches for Info with matching ID in the hash table.
    # Returns the Info if found, or None if not found.
    def search(self, ID):
        # get the index list where this ID would be.
        index = hash(ID) % len(self.table)
        index_list = self.table[index]
        #print(index_list)

        # search for the key in the bucket list
        for k in index_list:
            #print (Info)
            if k[0] == ID:
                return k[1] #Info

        return None

    # Removes Info with matching ID from the hash table.
    def remove(self, ID):
        # get the index list where this Info will be removed from.
        index = hash(ID) % len(self.table)
        index_list = self.table[index]

        # remove the Info from the index list if it is present.
        for k in index_list:
            #print (key_value)
            if k[0] == ID:
                index_list.remove([k[0],k[1]])

    #def printHashTable(self):
        #i = 0
        #for i in range(len(self.table)):
            #print(packageHash.search(i))

        #for i in range(len(self.table)):

            #print("Index %d\n" % i)
            #for j in self.table[i]:
            #    print(j[1])
        #print(self.table)
        #return
