import json

with open('precipitation.json') as file:
    precipitation = json.load(file)

results = {}

#1.2 Select all measurements for Seattle
seattle = {}
for measurement in precipitation:
    if measurement['station'] == 'GHCND:US1WAKG0038':
        if measurement['date'] not in seattle:
            seattle[measurement['date']] = measurement['value']
        else:
            seattle[measurement['date']] = seattle[measurement['date']] + measurement['value']
#print(seattle)

#1.3 Calculate the monthly precipitation for Seattle
total_monthly_precipitation = []
for month in range(1, 13):
    total_monthly_precipitation.append(sum([value for key, value in seattle.items() if int(key[5:7]) == month]))

#1.4 Save results to a JSON file
results = {"Seattle":
           {"station": "GHCND:US1WAKG0038",
            "state": "WA",
            "total_monthly_precipitation": total_monthly_precipitation
            }
        }
with open('results.json','w') as file:
    json.dump(results,file,indent=4)