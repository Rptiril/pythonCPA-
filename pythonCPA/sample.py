# list = ['A+','B+','O+','AB+','AB-','O-']

# size = len(list)

# for i in range (size):
#     print(list[i])

# # for i in range (0):
# #     print('yahooo!')

# list = []
# if list:
#     print(list)
# else:
#     print('No records found!')

# waiters = ['akbar','babar','jahngir','angrej','tipu','babar','babar','tipu','tipu','tipu','tipu','tipu','tipu']
# dict = {}

# for i in waiters:
#     dict[i] = 0
# print(dict)

# for i in waiters:
#     dict[i] += 1
# print(dict)

# for i in  dict:
#     print(i + '-' + str(dict[i]))

colorCode = ['V','I','B','G','Y','O','R']
colorVal = ['Violet','Indigo','Blue','Green','Yello','Orange','Red']
colorDict = {}
 
for i in range(len(colorCode)):
    colorDict[colorCode[i]] = colorVal[i]

# print(colorDict)
for k,v in colorDict.items():
    print(v,end = ', ')







