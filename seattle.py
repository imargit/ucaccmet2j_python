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

#1.3 Calculate the monthly precipitation for Seattle
total_monthly_precipitation = []
for month in range(1, 13):
    total_monthly_precipitation.append(sum([value for key, value in seattle.items() if int(key[5:7]) == month]))

#2.1 Calculate the annual precipitation for Seattle
total_yearly_precipitation = []
total_yearly_precipitation.append(sum([value for key, value in seattle.items() if int(key[0:4]) == 2010]))

#2.2 Calculate the relative monthly precipitation for Seattle
relative_monthly_precipitation =[]
for month in range(1, 13):
    relative_monthly_precipitation.append(sum([value for key, value in seattle.items() if int(key[5:7]) == month])/total_yearly_precipitation[0])

#1.4,2.2 Save results to a JSON file
results = {"Seattle":
           {"station": "GHCND:US1WAKG0038",
            "state": "WA",
            "total_monthly_precipitation": total_monthly_precipitation,
            "total_yearly_precipitation": total_yearly_precipitation,
            "relative_monthly_precipitation": relative_monthly_precipitation
            }
        }
with open('results.json','w') as file:
    json.dump(results,file,indent=4)