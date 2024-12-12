import csv
from CreateHashTable import *
from Package import *
from Truck import *

'''
Citing Sources: 
Pretty Printed. (2017, September 11). Reading CSV Files in Python [Video]. YouTube. 
    https://www.youtube.com/watch?v=efSjcrp87OY

'''

# Create empty hash table of package data
packageHash = ChainingHashTable()

distanceData = []               #Create empty list for distance
addressData = []                #Create empty list for addresses

# Function to read package CSV file and insert objects into hash table
def loadPackageData(fileName):
    with open(fileName) as packageData:     # Read CSV file
        reader = csv.reader(packageData)
        for row in reader:          # Put each piece of data in the appropriate attribute of package
            packageID = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            weight = row[6]
            notes = row[7]
            loadTime = None         # No packages are loaded on any trucks
            truck = None            # No packages are loaded on any trucks
            status = 'HUB'          # All packages start at the hub
            deliveryTime = None     # No packages are delivered yet

            # Create a package object
            package = Package(packageID, address, city, state, zip, deadline, weight, notes, loadTime, truck, status, deliveryTime)
            #print(package)

            # Insert package object into hash table
            packageHash.insert(packageID, package)

# Function to read distance data and put it in a list of lists
def loadDistanceData(fileName):
    with open(fileName) as csvFile:     # Read CSV file
        reader = csv.reader(csvFile)
        for row in reader:
            distanceData.append(row)    # Add distanceData to list

        # Fill in the whole distance table so distance from a to b is same as b to a
        for x in range(len(distanceData)):
            for y in range(len(distanceData)):
                distanceData[x][y] = distanceData[y][x]

# Create function to load the addresses into a list
def loadAddressData(fileName):
    with open(fileName) as csvFile:         # Read CSV file
        reader = csv.reader(csvFile)
        for row in reader:
            address = row[2]
            addressData.append(address)     # Add addresses to list