import json
from functools import reduce

with open('countries.json',mode="rt", encoding='utf-8') as file:
    data = json.load(file)

countries_with_cities = filter(lambda country: "cities" in country and country["cities"], data)

largest_city_data = map(
    lambda country: (
        country["name"], 
        max(country["cities"], key=lambda city: city["population"])["name"], 
        max(country["cities"], key=lambda city: city["population"])["population"]
    ), 
    countries_with_cities
)

largest_city_by_country = reduce(
    lambda acc, item: {**acc, item[0]: (item[1], item[2])},
    largest_city_data,
    {}
)

for country, (city, population) in sorted(largest_city_by_country.items()):
    print(f"{country}: {city} with population {population}")
