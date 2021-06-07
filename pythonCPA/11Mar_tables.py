class Table:
    def __init__(self,tableNo,WaiterName,Status):
        self.tableNo = tableNo
        self.waiterName = WaiterName
        self.status = Status

def findWaiterWaiseTotalNoOfTables(tableList):
    dict = {}
    for t in tableList:
        dict[t.waiterName] = 0

    for t in tableList:
        dict[t.waiterName] += 1
    return dict

def findWaiterNameByTableNo(tableList,tno):
    for t in tableList:
        if t.tableNo == tno:
            name = t.waiterName
            break

    if name:
        return name
    else:
        return None

n = int(input("Enter the number of table objects : "))
tableList = []
for i in range (n):
    tableNo = int(input(f"Enter table no for table object {i+1} : "))
    waiterName = input(f"Enter Waiter Name for table object {i+1} : ")
    status = input(f"Enter Order Status for table object {i+1} : ")
    obj = Table(tableNo,waiterName,status)
    tableList.append(obj)
tno = int(input("Enter the table number whose waiter name you want : "))
waitDic = findWaiterWaiseTotalNoOfTables(tableList)
name = findWaiterNameByTableNo(tableList,tno)

for key in sorted(waitDic.keys()):
    print(key + '-' + str(waitDic[key]))

if name is None:
    print('No Table Found')
else:
    print(name)

