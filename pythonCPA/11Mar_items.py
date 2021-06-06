class items:
    def __init__(self, itemName, itemType, unitPrice):
        self.itemName = itemName
        self.itemType = itemType
        self.unitPrice = unitPrice
    
class store:
    # itemInventory is dictionary having
    # itemsObj as key and its stock as value
    def __init__(self,  itemInventory):
        self.itemInventory = itemInventory
    
    # name id the name of item which you want to find in the itemInventory
    # reqQty is the quantity of items required
    def buyItems(self, name, reqQty): 
        for itemsObj,stock in self.itemInventory.items():
            if (itemsObj.itemName.lower() == name.lower() and stock == 0):
                return None
            if itemsObj.itemName.lower() == name.lower() and reqQty > stock:
                bill = itemsObj.unitPrice * stock
                itemInventory[itemsObj] = 0
                return bill
            if itemsObj.itemName.lower() == name.lower() and reqQty <= stock:
                bill = itemsObj.unitPrice * reqQty
                itemInventory[itemsObj] = stock - reqQty
                return bill
        return None


if __name__ == '__main__':
    n = int(input())
    itemInventory = {}
    for i in range (n):
        itemName = input()
        itemType = input()
        unitPrice = input()
        stock = int(input())
        itemObj = items(itemName, itemType, unitPrice)
        itemInventory[itemObj] = stock
    storeObj = store(itemInventory)
    m = int(input())
    itemsReq = {}
    for i in range (m):
        name = input()
        qty = int(input())
        itemsReq[name] = qty
    for name,qty in itemsReq.items():
        bill = storeObj.buyItems(name,qty)
        if bill == None:
            print(f'item {name} is not available')
        else:
            print(f'Bill of item {name} = {bill}')
    print('Stock in Hand:')
    for itemObj,stock in storeObj.itemInventory.items():
        print(f'{itemObj.itemName} {stock}')
    