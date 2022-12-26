class Database:
    def __init__ (self):
        self.db = {}
        
    def registNewCustomer(self, customer, name):
        if customer in self.db:
            return -1
        else:
            appenddic = {}
            appenddic.update({customer : name})
            self.db[customer] = name
            return appenddic
        
    def getCustomerNumber(self):
        l = 0
        for i in self.db:
            l += 1
        return l

    def getCustomerNameById(self, customer):
        if customer in self.db.keys():
            return {customer : self.db[customer]}
        else:
            return -1
       
    def getCustomerIDByName(self, name):
        if name in self.db.values():
            returndic ={}
            for key, value in self.db.items():
                if value == (name):
                    returndic[key] = name
            return returndic
        else:
            return -1 
        
    def getALLCustomer(self):
        return self.db
    
    def removeCustomerByID(self, customer):
        if customer in self.db.keys():
            del self.db[customer]
            return self.db
        else:
            return -1
    
    def removeCustomerByName(self, name):
        count = 0
        keys = []
        for key, value in self.db.items():
            if value == name:
                keys.append(key)
                count += 1

        if count != 0:
            for item in keys:
                self.db.pop(item)
            return self.db
        else:
            return -1
        
    def getALLCustoerNameSorted(self):
        namelist =[]
        for value in self.db.values():
            namelist.append(value)
        namelist.sort()
        return namelist
    
    def getALLCustomerIDSorted (self):
        customerlist =[]
        for key in self.db.keys():
            customerlist.append(key)
        customerlist.sort()
        return customerlist
    
    def getDuplicatedCustomerNames(self):
        for key in self.db.values():
            returndic = {}
            for key, value in self.db.items():
                if value == (name):
                    returndic[key] = name
            return returndic
        

            
        
        
            


    

