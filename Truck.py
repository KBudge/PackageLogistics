from DeliveryFunctions import *
from loadCSVData import packageHash

#Truck class
class Truck:
    #Constructor to initialize truck objects
    def __init__(self, truckID, packages, hour, minute):
        self.truckID = truckID                  #Truck number
        self.packages = packages                #List of packages on the truck
        self.hourLeftHub = hour                 #Hour the truck leaves the HUB
        self.minuteLeftHub = minute             #minute the truck leaves the HUB
        self.timeLeftHub = startTime(hour, minute) #Time and date truck left the HUB
        self.currentTime = self.timeLeftHub     #Current time of truck at location
        self.currentLocation = addressData[0]   #Current address of truck
        self.totDistance = 0.0                  #Keeps track of the total distance the truck has traveled
        self.maxCapacity = 16                   #Truck can carry 16 packages at most
        self.speed = 18                         #Truck speed is 18 mph

    # Prints the string for object instead of object reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" %(self.truckID, self.packages, self.timeLeftHub, self.currentTime, self.currentLocation, self.totDistance)

    #Function to load packages onto truck
    def loadPackages(self, packagesInList, truckNum):
        packageList = []    #Creates empty package list
        for ID in packagesInList:   #For each package loaded into the truck
            ID = int(ID)
            package = packageHash.search(ID)
            package.status = "EN ROUTE"         #Change package status to EN ROUTE
            package.truck = truckNum.truckID    #Add truck number to package
            package.loadTime = self.timeLeftHub #Add package load time
            packageHash.insert(ID, package)     #Update hash table with new package info
            packageList.append(packageHash.search(ID))  #Add package to list of packages in truck



