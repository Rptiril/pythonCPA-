'''
Create a class Traveler with below attributes:

travelerName String

traveledCountry: ( list of string type represents the names of the country the traveler has

travelled )

travelerAge int

countryFrom: string



Create a constructor which takes all the above attributes in the same sequence.



Define another class TravelAgency with below attributes:

travelerList: list of Traveler objects . 

and having the below member functions:



countTravelersTraveledCountry: Which takes a string representing the name of a country as input,
 and returns the count of travelers from the travelerList of TravelAgency who has travelled that country . 

getTravelerTravelledMaxCountry: Finds the traveler who has travelled highest number of countries 
and returns the name of that traveler. If more than one such travelers are there having the highest 
count of countries travelled method return the name of the traveler whose name appears first in the list 
as taken as input . 



Instructions to write main function:

a. You would require to write the main section completely. Hence please follow the below

instructions for the same.

b. You would require to write the main program which is 
inline to the "Sample input description section" mentioned below and to read the data in the same sequence.

c. Create the respective objects (Traveler and TravelAgency) with the given sequence of

arguments to fulfill the _init_method as mentioned in requirement defined in the respective

classes referring to the below instructions.

1. Create a list of travelers. To create the list, 
First read the number of travelers you want to store in the list.
repeats for the number of traveler to be added to the list

2. Read the values for the travelers. Create the Traveler object and add to the list. This point

a. First read the name of the traveler.

b. Then, read a number representing the count of countries travelled.

c. Read a string representing the name of the country and add to the list. 
This point repeats for the count taken in point #2.b above.

d. Finally, read values for travelerAge and country From.

ii. Create a TravelAgency object by using the list created in point #c1.

d. Read the name of the country to be  to the function count Travelers TraveledCountry.

e. Call the functions count Travelers Traveled Country by passing the value read in point #d as argument.

f. Call the function get Traveler Travelled MaxCountry

g: Print the value returned by the method count Travelers Traveled Country

h. Print the value returned by the method get Traveler Travelled MaxCountry.



Sample input description:

a. First line represents the integer value which represents the number of Traveler objects

b. Next lines of input represents one traveler specific data s below one by one in each 
line travelerName traveled Country list of country names): for this first the count of countries 
traveled is read followed by names of the countries to create the list traveler Age country From.

c. The Point #b repeats for the number of objects mentioned in the point #a.

d The last line of input is the name of the country to be passed as argument to the method

country Travelers TraveledCountry.



Sample Input : 

5
Sachin
4
Japan
Brazil
Chaina
Nepal
40
India
Kamini
4
Denmark
Australia
Indonesia
Ghana
37
Nepal
Saurav
6
Brazil
Bhutan
Afganisthan
UK
Nepal
Newzeland
32
Bangladesh
Ricky
3
Australia
Europe
Germany
42
UK
Dravid
2
India
Bhutan
39
Pakisthan
Australia


Sample Output :

2
Saurav
'''

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

    