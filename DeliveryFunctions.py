from CreateHashTable import *
from Package import *
from Truck import *
from loadCSVData import *
from datetime import datetime, timedelta



'''
Citing Sources:

C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor. WGU Course Search Resources.
	Retrieved July 22, 2024, from
    https://srm--c.vf.force.com/apex/coursearticle?Id=kA03x000001DbBGCA0

'''

#Look up the index of an address
def addressIndex(address):
    return addressData.index(address)

#Find the distance between two addresses using their indexes
def distanceBetween(address1, address2):
    if address1 not in addressData:         #Print error message if address is not in data
        return "Invalid first address"

    elif address2 not in addressData:       #Print error message if address is not in data
        return "Invalid second address"

    else:       #Returns the distance between two valid addresses
        x = addressIndex(address1)
        y = addressIndex(address2)
        #print(x, y)
        return float(distanceData[x][y])

#Formats the time the truck leaves the hub
def startTime(h, m):
    today = datetime.today()
    start = datetime(today.year, today.month, today.day, h, m)
    return start

#Function to deliver the packages
def delivering(truck):
    while len(truck.packages) > 0:  #Loops through all packages on the truck
        minDistance = 5000          #Variable to keep track of minimum distance
        nextPackage = None          #Keeps track of which package to deliver next

        #Loops through all the packages currently in the truck
        for ID in truck.packages:                   #Checks all packages in truck to see distance from current location
            ID = int(ID)
            package = packageHash.search(ID)
            truckAddress = truck.currentLocation        #Find the address the truck is at
            packageAddress = package.address            #Find the address of the package
            distance = distanceBetween(truckAddress, packageAddress)    #Find the distance between the 2 addresses

            if distance < minDistance:      #if distance is the smallest so far
                minDistance = distance      #assign the minDistance to that distance
                nextPackage = package       #assign that package to be delivered next

        truck.totDistance += minDistance                #add distance to the total distance truck has traveled
        truck.currentTime += timedelta(minutes=((minDistance/truck.speed) * 60))    #add minutes to time
        nextPackage.status = "DELIVERED"                #Update status of package to DELIVERED
        nextPackage.deliveryTime = truck.currentTime    #Update package delivery time
        truck.currentLocation = nextPackage.address     #Send truck to packages address
        truck.packages.remove(nextPackage.packageID)    #Remove package from list of packages that were loaded to truck


