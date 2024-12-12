
#Package class
class Package:
    #Constructor
    def __init__(self, packageID, address, city, state, zip, deadline, weight, notes, loadTime, status, deliveryTime, truck):
        self.packageID = packageID      # The package ID number
        self.address = address          # Number and street of where package needs to go
        self.city = city                # City where package needs to go
        self.state = state              # State where package needs to go
        self.zip = zip                  # Zip code where package needs to go
        self.deadline = deadline        # The Max time package needs to be delivered by
        self.weight = weight            # Weight of the package
        self.notes = notes              # Notes about the package
        self.loadTime = loadTime        # Time package was loaded on a truck
        self.truck = truck              # Truck number package is on
        self.status = status            # The current status of the package ('HUB', 'EN ROUTE', 'DELIVERED')
        self.deliveryTime = deliveryTime # The time the package was delivered


    # Prints the string for object instead of object reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s %s, %s" % (self.packageID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.loadTime, self.truck, self.status, self.deliveryTime)


