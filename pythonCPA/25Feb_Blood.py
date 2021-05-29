class Blood:
    
    def __init__(self,bloodGroup,unitInHand):
        self.bloodGroup = bloodGroup
        self.unitInHand = unitInHand


class BloodBank:
    
    def __init__(self,bloodList):
        self.bloodList = bloodList

    def isBloodAvailable(self,bg,unitReq):
        for b in self.bloodList:
            if (b.bloodGroup == bg) and (b.unitInHand >= unitReq):
                return True
        return False

    def findMinBloodStock(self):
        MinBloodStockList = []
        bloodObj = self.bloodList[0]
        min = bloodObj.unitInHand
        
        for b in self.bloodList:
            if b.unitInHand < min:
                min = b.unitInHand
         
        for b in self.bloodList:
            if b.unitInHand == min:
                MinBloodStockList.append(b.bloodGroup)
        return MinBloodStockList


if __name__ == '__main__':
    
    n = int(input())
    bloodList = []
    
    for i in range (n):
        bloodGroup = input()
        unitInHand = int(input())
        bloodObj = Blood(bloodGroup,unitInHand)
        bloodList.append(bloodObj)
    
    bg = input()
    unitReq = int(input())

    b = BloodBank(bloodList)
    val = b.isBloodAvailable(bg,unitReq)
    if val:
        print('Blood Available')
    else:
        print('Blood not Available')
    
    list = b.findMinBloodStock()
    size = len(list)
    for i in range(size):
        print(list[i])
    
