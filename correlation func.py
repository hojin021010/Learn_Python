
import math
class baseratecorr:
    
    def __init__(self, datalist1, datalist2):
        self.datalist1 = datalist1
        self.datalist2 = datalist2
        
    def mean(self,data):
        result = 0
        self.data = data
        len_data = len(self.data)
        for i in self.data:
          result += i
        return result / len_data  

    def correlation(self, data1, data2):
        meanData1 = self.mean(data1)
        meanData2 = self.mean(data2)
        up = 0
        for i in range(len(data1)):
            up += (data1[i]-meanData1) * (data2[i]-meanData2)
        bottom = 0
        data1Bottom = 0
        data2Bottom = 0
        for i in data1:
            data1Bottom += (i - meanData1)**2
        for i in data2:
            data2Bottom += (i - meanData2)**2
        bottom = math.sqrt(data1Bottom) * math.sqrt(data2Bottom)
        return up/bottom

 
 