import requests
import csv

data = []

with open("springerbooks.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)



for i in range(0, len(data)):
    if data[i][0].isnumeric:
        if (i+1 < len(data)):
            print (data[i+1])
            i = i+1