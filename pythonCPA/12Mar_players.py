class Player:
  def __init__(self,name,playedCountry,age,countryFrom):
    self.name = name
    self.playedCountry = playedCountry
    self.age = age
    self.countryFrom = countryFrom
  
def countPlayers(playersList, country):
  count = 0
  for player in playersList:
    if player.countryFrom.lower() == country.lower():
      count+=1
  return count

def getPlayerPlayedforMaxCountry(playersList):
  max = 0
  for player in playersList:
    if (len(player.playedCountry) > max):
      max = len(player.playedCountry)
  for player in playersList:
    if(len(player.playedCountry) == max):
      name = player.name
  return name

if __name__ == '__main__':
  n=int(input())
  playerList = []
  for i in range (n):
    name = input()
    countCountry = int(input())
    playedCountry = []
    for j in range (countCountry):
      country = input()
      playedCountry.append(country)
    age = int(input())
    countryFrom = input()
    playerObj = Player(name, playedCountry, age, countryFrom)
    playerList.append(playerObj)
  country = input()
  count = countPlayers(playerList, country)
  name = getPlayerPlayedforMaxCountry(playerList)
  print(count)
  print(name)