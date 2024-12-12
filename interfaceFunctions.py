from datetime import datetime
from Package import *
from DeliveryFunctions import *
from loadCSVData import *

#Function to format the users input time
def inputTime(h, m):
    today = datetime.today()
    inputTime = datetime(today.year, today.month, today.day, h, m, 0, 0)
    return inputTime

#Function to print one packages' information at the users input time
def packageAtTime(ID, time):
    packageID = ID
    statusTime = time
    package = packageHash.search(packageID)

    if packageID == 9:
        #If user enters time at or after 10:20 package 9 will have updated address
        if statusTime >= startTime(10,20):
            package.address = '410 S State St'
            package.zip = '84111'
        else:           #If time before 10:20 package 9 will have wrong address
            package.address = '300 State St'
            package.zip = '84103'

    if package.loadTime > time:     #Prints if package has not be loaded on a truck at user input time
        print("%s | %s, %s, %s, %s | %s kg | %s | %s | Not Loaded | HUB" %(packageID, package.address, package.city, package.state, package.zip, package.weight, package.notes, package.deadline))

    #Prints if package has been loaded on the truck but not yet delivered at user input time
    elif statusTime >= package.loadTime and statusTime < package.deliveryTime:
        print("%s | %s, %s, %s, %s | %s kg | %s | %s | Loaded on Truck %s at %s | EN ROUTE" %(packageID, package.address, package.city, package.state, package.zip, package.weight, package.notes, package.deadline, package.truck, package.loadTime))

    #Prints if package has already been delivered before or at user input time
    elif statusTime >= package.deliveryTime:
        print("%s | %s, %s, %s, %s | %s kg | %s | %s | Loaded on Truck %s at %s | DELIVERED at %s" %(packageID, package.address, package.city, package.state, package.zip, package.weight, package.notes, package.deadline, package.truck, package.loadTime, package.deliveryTime))

    return