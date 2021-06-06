class Item:
	def __init__(self, iname,it,up):
		self.itemName= iname
		self.itemType=it
		self.unitPrice=up
class Store:
	def __init__(self,itemlist):
		self.itemInventory=itemlist
	def buyItem(self,item,quantity):
		for items,quantityInHand in itemInventory.items():
			if(items.itemName.lower()==item.lower() and quantity==0):
				return None
			if(items.itemName.lower()==item.lower() and quantity>quantityInHand):
				itemInventory[items]=0
				return items.unitPrice*quantityInHand
			if(items.itemName.lower()==item.lower() and quantity<=quantityInHand):
				itemInventory[items]=quantityInHand-quantity
				return items.unitPrice*quantity
		return None
if __name__=="__main__":
	num=int(input())
	itemInventory={}
	for i in range(num):
		itemName=input()
		itemType=input()
		unitPrice=int(input())
		quantityInHand=int(input())
		itemInventory[Item(itemName,itemType,unitPrice)]=quantityInHand
	store1=Store(itemInventory)
	order={}
	num=int(input())
	for i in range(num):
		itemName=input()
		quantity=int(input())
		order[itemName]=quantity
	for itemName,quantity in order.items():
		billAmount=store1.buyItem(itemName,quantity)
		if(billAmount==None):
			print(itemName,"is not available")
		else:
			print("Bill of the item ",itemName,"=",billAmount)
	print("Stock in Hand:")
	for item,quantityInHand in store1.itemInventory.items():
		print(item.itemName,quantityInHand,sep=" ")