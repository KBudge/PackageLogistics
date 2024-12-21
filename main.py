from Truck import *
from interfaceFunctions import *


# Function to print out data in hash table
def printHashTable():
    i = 1
    while i <= 40:
        print(packageHash.search(i))
        i += 1

# Function to total up the miles of all trucks
def totalMiles():
    total = round(truck1.totDistance + truck2.totDistance + truck3.totDistance, 2)
    return total

# Calls function to retrieve data from package CSV file
loadPackageData("CSV/packageCSV.csv")
loadDistanceData("CSV/distanceCSV.csv")
loadAddressData("CSV/addressCSV.csv")

# List of packages for truck one
packages1 = [13, 14, 15, 16, 19, 20, 21, 34, 39, 1, 4, 40, 8, 30, 37]
truck1 = Truck(1, packages1, 8, 0)  # Create truck1 object
truck1.loadPackages(packages1, truck1)                  # Calls function to load packages onto truck 1
delivering(truck1)                                      # Calls function to deliver packages from truck 1

# List of packages for truck two
packages2 = [3, 18, 36, 38, 5, 9, 10, 11, 12, 23, 27, 35]
truck2 = Truck(2, packages2, 10, 20)# Create truck2 object
truck2.loadPackages(packages2, truck2)                  # Calls function to load packages onto truck 2
update9 = packageHash.search(9)         #Get package 9 information

if update9.loadTime != 'NONE':
    update9.address = '410 S State St'      #Change package 9 address to correct address
    update9.city = 'Salt Lake City'
    update9.state = 'UT'
    update9.zip = '84111'

delivering(truck2)                                      # Calls function to deliver packages from truck 2

# List of packages for truck three
packages3 = [6, 25, 26, 31, 32, 7, 29, 17, 28, 2, 33, 24, 22]
truck3 = Truck(3, packages3, 9, 5)  # Create truck3 object
truck3.loadPackages(packages3, truck3)                  # Calls function to load packages onto truck 3
delivering(truck3)                                      # Calls function to deliver packages from truck 3

# Begin User Interface
class main:
    # Print interface menu
    print("\nWelcome to the interface for Western Governors University Parcel Service (WGUPS)\n")
    print("MENU\n")
    print("Please consider the following menu options carefully:")
    print("****************************")
    print("Enter '1' to print all the information of all packages and total miles traveled after deliveries are complete")
    print("Enter '2' to print the status of ONE package at a certain time")
    print("Enter '3' to print all the information of all packages at a certain time")
    print("Enter '0' to exit menu")
    print("****************************\n")

    quitStatus = True
    while quitStatus is True:
        option = int(input("Enter Option Number here: "))   #Ask user to pick menu option

        if option == 1:             #If user picks option 1
            for i in range(1, 41):  #For every package in hash table, print info and delivery time
                package = packageHash.search(i)
                pID = str(package.packageID)
                pStatus = str(package.status)
                pDelTime = str(package.deliveryTime)

                print("%s | %s, %s, %s, %s | %s kg | %s | Truck %s | %s | DELIVERED at %s" %(pID, package.address, package.city, package.state, package.zip, package.weight, package.notes, package.truck, package.deadline, package.deliveryTime))

            #Prints total distance the trucks traveled
            print("\nTotal distance all trucks traveled: " + str(totalMiles()))
            quitStatus = False      #Exits the program

        elif option == 2:       #If user picks option 2
            inputHour = int(input("Enter hour from 0-23: "))     #Asks user for an hour
            if inputHour not in range(0, 24):       #Exits program if input is out of range
                print("Invalid input, please run program again")
                exit()

            inputMinute = int(input("Enter minute from 0-59: ")) #Asks user for minute
            if inputMinute not in range(0, 60):     #Exits program if minute is not in range
                print("Invalid input, please run program again")
                exit()

            inputPackage = int(input("Enter package number from 1-40: ")) #Asks user for package number
            if inputPackage not in range(1, 41):     #Exits program if package number is not in range
                print("Invalid input, please run program again")
                exit()

            time = inputTime(inputHour, inputMinute)    #Calls function to properly format the time
            #Specifies the time the user wants to know package status'
            print("All information for Package %s at %s:" %(inputPackage, time))
            #Prints a heading for user to know what details from the packages will be printing
            print("Package ID | Address, City, State, Zip Code | Weight | Notes | Deadline | Truck Number and Loaded Time | Status")
            packageAtTime(inputPackage, time)  #Calls function to print one packages info at input time

            quitStatus = False      #Exits program

        elif option == 3:       #If user picks option 3
            inputHour = int(input("Enter hour between 0-23: "))     #Asks user for an hour
            if inputHour not in range(0, 24):       #Exits program if input is out of range
                print("Invalid input, please run program again")
                exit()

            inputMinute = int(input("Enter minute between 0-59: ")) #Asks user for minute
            if inputMinute not in range(0, 60):     #Exits program if minute is not in range
                print("Invalid input, please run program again")
                exit()

            time = inputTime(inputHour, inputMinute)    #Properly formats the time
            #Specifies the time the user wants to know package status'
            print("All packages information at %s:" %time)
            #Prints a heading for user to know what details from the packages will be printing
            print("Package ID | Address, City, State, Zip Code | Weight | Notes | Deadline | Truck Number and Loaded Time | Status")

            #Loops through all packages
            for i in range(1, 41):
                packageAtTime(i, time)  #Calls function from interface Functions

            quitStatus = False      #Exits program

        elif option == 0:           #Exits program if user picks 0
            quitStatus = False      #Exits program

        #If user inputs anything except 0, 1, or 2, user will be prompted to make another choice
        else:
            print("Invalid input, please try again")


