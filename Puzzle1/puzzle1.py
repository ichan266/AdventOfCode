filename = "puzzle1-input.txt"

with open(filename) as f:
    content = f.readlines()

years = [int(year) for year in content]


def findProduct(years):
    """ Taken in a list of year, find the two years that adds up to 2020, then return the sum."""

    for year in years:
        diff = 2020 - year
        if diff in years:
            return year * diff


print(findProduct(years))
