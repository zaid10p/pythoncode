import json

json_list = []      # store the converted json data for each line
csv_file = open('temp/csv_file.txt', 'r')


for line in csv_file.readlines():
    # first get rid of the \n and then split with ','
    club, city, country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

with open('temp/json_file.txt', 'w') as json_file:
    json.dump(json_list, json_file)


# convert dict to json String
print(json_list)
print(type(json.dumps(json_list)))

print(json.loads('["a","b"]'))