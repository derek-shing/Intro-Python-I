# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self,name,lat, lon):
        LatLon.__init__(self,lat,lon)
        self.name = name

    def print_Waypoint(self):
        print(self.name, self.lat, self.lon)

    def __str__(self):
        return (f"{self.name}, {self.lat}, {self.lon}")


# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self,name,difficulty,size,lat,lon):
        Waypoint.__init__(self,name,lat,lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return(f"{self.name}, diff {self.difficulty}, size {self.size}, {self.lat}, {self.lon}")


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs",41.70505,-121.51521)
waypoint.print_Waypoint()

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)
