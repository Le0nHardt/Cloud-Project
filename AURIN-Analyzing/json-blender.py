# This file is for

import json

with open('/Users/hayden/Desktop/Alldata/SydneyAgedRate.json', 'r') as f:
    data = json.load(f)
    print(len(data["features"]))
    for xx in data["features"]:
        print(xx["properties"])

    xx = data["features"][0]["properties"]
    # print(xx)

    print(type(data["features"][0]["properties"]["area_code"]))

    listOfKey = []

    # print(isinstance(xx, dict))
    for (key, value) in xx.items():
        if isinstance(value, int):
            listOfKey.append(key)

    # print(listOfKey)

    dddict = {}

    for propertyName in listOfKey:
        dddict[propertyName] = 0

    # print()
    # print(dddict)

    yy = data["features"][0]

    for xx in data["features"]:
        for (key, value) in xx["properties"].items():
            if isinstance(value, int):
                dddict[key] += value
    print(dddict)

# def foldProperties(dic1, dic2):
#     newDic = {}
#     for (key, value) in dic1.items():
#         newDic[key] = dic1[key] + dic2[key]
#
#     return newDic


