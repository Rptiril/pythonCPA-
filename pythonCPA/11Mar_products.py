class Product:
    
    def __init__(self,productName, productType,unitPrice,qtyOnHand):
        self.productName = productName.lower()
        self.productType = productType.lower()
        self.unitPrice = unitPrice
        self.qtyOnHand = qtyOnHand
    
class Store:
    
    def __init__(self,productList):
        self.productList = productList

    def purchaseProduct(self,name,qtyToBuy):
        name = name.lower()
        for p in self.productList:
            if (p.productName == name) and (p.qtyOnHand >= qtyToBuy):
                bill = p.unitPrice * qtyToBuy
                p.qtyOnHand -= qtyToBuy
                return bill
            
            if (p.productName == name) and (qtyToBuy > p.qtyOnHand):
                bill = p.unitPrice * p.qtyOnHand  
                p.qtyOnHand = 0
                return bill
            
            if (p.productName == name) and (p.qtyOnHand == 0):
                return None
        return None

if __name__ == '__main__':
    n = int(input())
    
    productList = []
    for i in range (n):
        productName = input()
        productType = input()
        unitPrice = int(input())
        qtyOnHand = int(input())
        productObj = Product(productName,productType,unitPrice,qtyOnHand)
        productList.append(productObj)
    
    name = input()
    qtyToBuy = int(input())
    
    s = Store(productList)
    bill = s.purchaseProduct(name,qtyToBuy)
    if bill:
        print(f'Product Available :)\nbill = {bill}')
    else:
        print('Product not available')
    
    for p in productList:
        print(f'{p.productName} {p.qtyOnHand}')

