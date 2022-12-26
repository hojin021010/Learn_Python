class Server:
    
    def __init__(self):
        self.l = []
        
    def makeOrder(self, ordernum, orders):
        count = 0
        if len(self.l) != 0:
            for i in self.l:
                if i[0] == ordernum:
                    count +=1
        
        if count == 0:
            apl = []
            apl.append(ordernum)
            apl.append(orders)
            self.l.append(apl)
            return apl
        else:
            return -1
    
    def getWaitingTime(self, ordernum, time):
        count = 0 
        for i in self.l:
            if i[0] == ordernum:
                count +=1
        if count != 0 :
            index = 0
            for i in self.l:
                if i[0] == ordernum:
                    index += 1
                    break
                else:
                    index += 1
            return time*index
        
    def serveOrder(self):
        k = self.l.pop(0)
        return k[0], k[1] 
    
    def getOrderNumber(self):
        count = 0
        for i in self.l:
            count +=1
    
    def cancelOrder(self, ordernum):
        count = 0 
        idex = 0
        for i in self.l:
            if i[0] == ordernum:
                count +=1
                break
            else:
                index +=1
        if count != 0:
            k = self.l[index]
            del self.l[index]
            return k[0], k[1]
        else :
            return -1, -1 
        
    def makeOrderVIP(self,ordernum,orders):
        count = 0 
        for i in self.l:
            if i[0] == ordernum:
                count +=1
                break
        if count != 0:
            return -1
        else:
            apl = [ordernum, orders]
            self.l.insert(0,apl)
            return apl
    
    def giveService(self, ordernum, service):
        count = 0 
        idex = 0
        for i in self.l:
            if i[0] == ordernum:
                count +=1
                break
            else:
                index +=1
        if count != 0 :
            new = self.l[index]
            new[1].append(service)
            self.l[index] = new
            return new[0], new[1]
        else:
            return -1, -1
            
    
    def getOrderItems(self):
        count = 0 
        for i in self.l:
            count +=1
        return count
                
          
            
            

 
    

            
            
        