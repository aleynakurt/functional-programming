import json
from functools import reduce

with open('countries.json',mode="rt", encoding='utf-8') as file:
    data = json.load(file)

valid_countries = list(filter(lambda x: x["population"] > 0 and x["surfaceArea"] > 0, data))

density_mapping = list(map(lambda x: (x, x["population"] / x["surfaceArea"]), valid_countries))

highest_density_country = reduce(lambda a, b: a if a[1] > b[1] else b, density_mapping)[0]

print(highest_density_country)