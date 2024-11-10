import json
from functools import reduce

with open('countries.json',mode="rt", encoding='utf-8') as file:
    data = json.load(file)

continent_life_expectancy = list(
    map(lambda country: (country["continent"], country["lifeExpectancy"]),
        filter(lambda country: country.get("lifeExpectancy") is not None, data))
)

def continent_counts(continent_total, val):
    continent, life_expectancy = val
    if continent in continent_total:
        continent_total[continent]["total_life"] += life_expectancy
        continent_total[continent]["count"] += 1
    else:
        continent_total[continent] = {"total_life": life_expectancy, "count": 1}
    return continent_total

continent_totals = reduce(continent_counts, continent_life_expectancy, {})

average_life_expectancy = {
    continent: continent_totals[continent]["total_life"] / continent_totals[continent]["count"]
    for continent in continent_totals
}

for continent in sorted(average_life_expectancy.keys()):
    print(f"{continent}: {average_life_expectancy[continent]}")