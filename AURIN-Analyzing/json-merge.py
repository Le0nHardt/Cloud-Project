import json

# AURIN dataset 1

dic_popu = {}
dic_emp_pop = {}
dic_unemp_pop = {}
dic_unemp = {}
dic_emp = {}
population_sum = 0


with open('/Users/hayden/Desktop/Alldata/MelbourneAgeDis.json', 'r') as f:
    data = json.load(f)
    for xx in data["features"]:
        # print(xx["properties"]["area_code"], " --- ", end = "")
        # print(xx["properties"]["x85pl_p_2_denom_6_13_6_13"])
        dic_popu[xx["properties"]["area_code"]] = xx["properties"]["x85pl_p_2_denom_6_13_6_13"]
        dic_emp_pop[xx["properties"]["area_code"]] = 0
        dic_unemp_pop[xx["properties"]["area_code"]] = 0
        dic_emp[xx["properties"]["area_code"]] = 0
        dic_unemp[xx["properties"]["area_code"]] = 0
        population_sum += xx["properties"]["x85pl_p_2_denom_6_13_6_13"]




# AURIN dataset 2

with open('/Users/hayden/Desktop/Alldata/MelbourneOccRate.json', 'r') as f:
    data = json.load(f)
    for xx in data["features"]:
        # print(xx["properties"]["SA2_Code_2011"], " --- ", end="")
        # print(xx["properties"]["Unemployment_rate"])
        if xx["properties"]["Unemployment_rate"] is not None:
            dic_unemp[xx["properties"]["SA2_Code_2011"]] = xx["properties"]["Unemployment_rate"]
        else:
            dic_unemp[xx["properties"]["SA2_Code_2011"]] = 0
        if xx["properties"]["Employment_to_population_ratio"] is not None:
            dic_emp[xx["properties"]["SA2_Code_2011"]] = xx["properties"]["Employment_to_population_ratio"]
        else:
            dic_emp[xx["properties"]["SA2_Code_2011"]] = 0

    # print(dic_unemp)
    # print(dic_emp)
    # print()
    # print(dic_popu)

for (code, population) in dic_popu.items():
    dic_emp_pop[code] = population * dic_emp[code]
    dic_unemp_pop[code] = population * dic_unemp[code]

# print(dic_emp_pop)
# print(dic_unemp_pop)

employment_pop = 0
unemployment_pop = 0

for (_, value) in dic_emp_pop.items():
    employment_pop += value

for (_, value) in dic_unemp_pop.items():
    unemployment_pop += value


employment_pop = round(employment_pop)
unemployment_pop = round(unemployment_pop)

print("unemployment population: ", unemployment_pop)
print("employment population: ", employment_pop)
print("population: ", population_sum)
print("unemp rate: ", unemployment_pop/population_sum)
print("emp rate: ", employment_pop/population_sum)


# SA2_Code_2011
# Unemployment_rate
# Employment_to_population_ratio
