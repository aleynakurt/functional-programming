import json
from functools import reduce

with open('countries.json',mode="rt", encoding='utf-8') as file:
    data = json.load(file)

countries_with_continent = filter(lambda country: country.get("continent") is not None, data)

continent_city_counts = map(
    lambda country: (country["continent"], len(country.get("cities", []))),
    countries_with_continent
)

city_count_by_continent = reduce(
    lambda acc, item: {
        **acc,
        item[0]: acc.get(item[0], 0) + item[1]
    },
    continent_city_counts,
    {}
)

for continent in sorted(city_count_by_continent.keys()):
    print(f"{continent}: {city_count_by_continent[continent]}")
