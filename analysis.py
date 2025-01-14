import json
import pandas as pd

with open('precipitation.json') as file:
    precipitation = json.load(file)

#3.1 Read the CSV file
station = pd.read_csv('stations.csv',usecols=['Location','State','Station'])
# Create a dictionary with locations as keys and station ids as values
locations = {}
for index, row in station.iterrows():
    locations[row['Location']] = row['Station']

results = {}

for location in locations:
    print(location)
    #1.2 Select all measurements for the city
    city = {}
    for measurement in precipitation:
        if measurement['station'] == locations[location]:
            if measurement['date'] not in city:
                city[measurement['date']] = measurement['value']
            else:
                city[measurement['date']] = city[measurement['date']] + measurement['value']

    #1.3 Calculate the monthly precipitation for the city
    total_monthly_precipitation = []
    for month in range(1, 13):
        total_monthly_precipitation.append(sum([value for key, value in city.items() if int(key[5:7]) == month]))

    #2.1 Calculate the annual precipitation for the city
    total_yearly_precipitation = []
    total_yearly_precipitation.append(sum([value for key, value in city.items() if int(key[0:4]) == 2010]))
    #2.2 Calculate the relative monthly precipitation for the city
    relative_monthly_precipitation =[]
    for month in range(1, 13):
        relative_monthly_precipitation.append(sum([value for key, value in city.items() if int(key[5:7]) == month])/total_yearly_precipitation[0])

    #1.4,2.2 Save results to a JSON file
    results[location] = {
        "station": locations[location],
        "state": "WA",
        "total_monthly_precipitation": total_monthly_precipitation,
        "total_yearly_precipitation": total_yearly_precipitation,
        "relative_monthly_precipitation": relative_monthly_precipitation
        }
    with open('results.json','w') as file:
        json.dump(results,file,indent=4)