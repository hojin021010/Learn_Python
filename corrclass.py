# 두 리스트를 class 객체로 만들었을 때 상관관계를 구할 수 있다.
import math 

class baseratecorr:
    
    def __init__(self, datalist1, datalist2):
        self.datalist1 = datalist1
        self.datalist2 = datalist2  

    def correlation(self):
        meanData1 = math.mean(self.datalist1)
        meanData2 = math.mean(self.datalist2)
        up = 0
        for i in range(len(self.datalist1)):
            up += (self.datalist1[i]-meanData1) * (self.datalist2[i]-meanData2)
        bottom = 0
        data1Bottom = 0
        data2Bottom = 0
        for i in self.datalist1:
            data1Bottom += (i - meanData1)**2
        for i in self.datalist2:
            data2Bottom += (i - meanData2)**2
        bottom = math.sqrt(data1Bottom) * math.sqrt(data2Bottom)
        return up/bottom