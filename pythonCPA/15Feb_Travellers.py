
class Traveler:
    def __init__(self,travelerName,traveledCountry,travelerAge,countryFrom):
        self.travelerName = travelerName
        self.traveledCountry = traveledCountry
        self.travelerAge = travelerAge
        self.countryFrom = countryFrom

class TravelAgency:
    def __init__(self,travelerList):
        self.travelerList = travelerList
    
    def countTravelersTraveledCountry(self,country):
        count = 0
        for t in self.travelerList:
            for c in t.traveledCountry:
                if c == country:
                    count +=1
        return count
    
    def getTravelerTraveledMaxCountry(self):
        size = 0
        for traveler in self.travelerList:
            if len(traveler.traveledCountry) > size:
                size = len(traveler.traveledCountry)
            
        for traveler in self.travelerList:
            if len(traveler.traveledCountry) == size:
                return traveler.travelerName

if __name__ == "__main__":
    noOfTravelers = int(input())
    travelerList = []
    
    for i in range(noOfTravelers):
        travelerName = input()
        noOfCountriesTraveled = int(input())
        traveledCounty = []
        for j in range(noOfCountriesTraveled):
            countryName = input()
            traveledCounty.append(countryName)
        travelerAge = int(input())
        countryFrom = input()
        travelerList.append(Traveler(travelerName,traveledCounty,travelerAge,countryFrom))
    
    country = input()
    obj = TravelAgency(travelerList)

    print(obj.countTravelersTraveledCountry(country))
    print(obj.getTravelerTraveledMaxCountry())

    