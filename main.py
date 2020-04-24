import csv

with open('./dati/01_sites.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        pass
        #print(', '.join(row))
        #print(row)
        #print(type(row))


with open('./dati/01_topology.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        pass
        #print(', '.join(row))
        #print(row)
        #print(type(row))


with open('./dati/01_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        #print(', '.join(row))
        print(row)
        #print(type(row))