from typing import Literal


class Container:
    
    def __init__(self,id,length,breadth,height,pricePerSqrFt):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.pricePerSqrFt = pricePerSqrFt
    
    def findVolume(self):
        volume = self.length * self.breadth * self.height
        return volume
    

class PackingCompany:

    def __init__(self,containerList):
        self.containerList = containerList
    
    def findContainerCost(self,containerId):
        for c in self.containerList:
            if c.id == containerId:
                return c.findVolume() * c.pricePerSqrFt
        return None
    
    def findLargestContainer(self):
        l = 0
        for c in self.containerList:
            if c.findVolume() > l:
                l = c.findVolume()
        for c in self.containerList:
            if c.findVolume() == l:
                return c
    

if __name__ == "__main__":
    
    n = int(input())
    containerList = []
    
    for i in range (n):
        id = int(input())
        length  = int(input())
        breadth = int(input())
        height  = int(input())
        pricePerSqrFt = int(input())
        containerObj = Container(id,length,breadth,height,pricePerSqrFt)
        containerList.append(containerObj)


    containerId = int(input())
    c = PackingCompany(containerList)
    val = c.findContainerCost(containerId)
    if val:
        print(val)
    else:
        print('No container found')
    
    obj = c.findLargestContainer()
    print(f'{obj.id} {obj.findVolume()}')