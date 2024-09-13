import csv

with open('./iris_data.txt') as f:
    data = [tuple(line) for line in csv.reader(f)]

print(data)
