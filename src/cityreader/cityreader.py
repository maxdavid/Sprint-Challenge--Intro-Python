# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
from style import color

cities = []


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"{self.name}: ({self.lat}, {self.lon})"

    def __str__(self):
        return f"{color.GREEN}{self.name}{color.END} ({self.lat}, {self.lon})"


def cityreader(cities=[]):
    with open("cities.csv") as file:
        rows = csv.reader(file, delimiter=",")
        next(rows)
        for row in rows:
            cities.append(City(row[0], float(row[3]), float(row[4])))

        return cities


# cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
# print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)


def find_cities_within(cities=[]):
    print(
        "Enter two sets of latitude/longitude points and find the cities that fall between!"
    )
    try:
        lat1, lon1 = input("Enter your first lat, lon (separated by a comma): ").split(
            ","
        )
        lat2, lon2 = input("Enter your second lat, lon (separated by a comma): ").split(
            ","
        )
    except ValueError:
        print(
            f"\n{color.RED}{color.BOLD}Not enough values specified!{color.END} \nQuitting."
        )
        return

    try:
        lat1, lon1, lat2, lon2 = (
            float(lat1.strip()),
            float(lon1.strip()),
            float(lat2.strip()),
            float(lon2.strip()),
        )
    except ValueError:
        print(
            f"\n{color.RED}{color.BOLD}Not valid numeric lat/lon coordinates!{color.END} \nQuitting."
        )
        return

    print()
    print(f"{color.BOLD}Cities within your specified lat/lon:{color.END}")
    [print(city) for city in cityreader_stretch(lat1, lon1, lat2, lon2, cities)]


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    def check_city_within(city):
        # return True if city is within the lat/lon bounds given by the user
        return (
            city.lat <= max(lat1, lat2)
            and city.lat >= min(lat1, lat2)
            and city.lon <= max(lon1, lon2)
            and city.lon >= min(lon1, lon2)
        )

    return [city for city in cities if check_city_within(city)]


find_cities_within(cityreader(cities))
