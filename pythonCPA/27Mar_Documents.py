class Document:
  def __init__(self,docId,docName,docDetails):
    self.docId = docId # type int
    self.docName = docName # type str
    self.docDetails = docDetails # type str
  
class DocumentArchive:
  def __init__(self,arachiveId,docList):
    self.arachiveId = arachiveId
    self.docList = docList
  
  def findDateFromDocumentDetails(self):
    thisList = []
    for d in self.docList:
      x = d.docDetails
      if x.count('/') == 2:
        l = x.split(',')
        for item in l:
          if '/' in item:
            thisList.append((d.docId,item))
    return thisList
  
  def countDocumnentsOfGivenType(self,dTname):
    count = 0
    for d in self.docList:
      x = d.docName.split('.')[1]
      if (x == dTname):
        count+=1
    return count
    

if __name__ == '__main__':
  n = int(input())
  docList = []
  for i in range (n):
    docId = int(input())
    docName = input()
    docDetails = input()
    docObj = Document(docId,docName,docDetails)
    docList.append(docObj)
  arachiveId = 7
  dAobj = DocumentArchive(arachiveId,docList)
  thisList = dAobj.findDateFromDocumentDetails()
  dTname = input()
  count = dAobj.countDocumnentsOfGivenType(dTname)
  for i in thisList:
    print(i[0],i[1])
  print(f"Document Count = {count}")
  