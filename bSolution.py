import csv
import os

import networkx as nx

G = nx.DiGraph()
lEdg = []
node = []
edge = []
comm = []
com2 = []

if os.path.exists('./solve1/05_giorno_solution2.csv'):
    print("CANCELLATO ./solve1/05_giorno_solution2.csv")
    os.remove('./solve1/05_giorno_solution2.csv')

# NODI
# Parametro 1: ID nodo
# Parametro 2: Nome nodo
with open('./dati/01_sites.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_node(row[0], name=row[1])
        node.append(row)

# ARCHI
# Parametro 1: ID nodo sorgente
# Parametro 2: ID nodo destinazione
# Parametro 3: Capacità arco
with open('./dati/01_topology.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_edge(row[0], row[1], cap=int(row[2]))
        edge.append(row)

# COMMODITIES
# Parametro 1: ID Sorgente
# Parametro 2: ID Destinazione
# Parametro 3: Banda richiesta
# Parametro 4: Priotrità
# Parametro 5: ID Commodities
with open('./dati/01_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        comm.append(row)

j = 0
with open('./dati/01_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = j
        com2.append(row)
        j = j+1

edge = [row + [0] for row in edge]
edge = [row + [0] for row in edge]

i = 0
for row in edge:
    row[4] = i
    i = i+1

i = 0
for row in comm:
    row[4] = i
    i = i+1

solT = False


for row in comm:
    print(row[4])
    with open('./out1/'+str(row[4])+'.csv', newline='') as csvfile:
        row_count = sum(1 for row in csvfile)
        print(row_count)
    with open('./out1/'+str(row[4])+'.csv', newline='') as csvfile:
        path = csv.reader(csvfile, delimiter=' ')
        inc = 1
        for elem in path:
            edgeTemp = [x[:] for x in edge]
            solT = False
            print(elem)
            for incr in range(len(elem)-1):
                for count in range(len(edgeTemp)):
                    if elem[incr] == edgeTemp[count][0] and elem[incr+1] == edgeTemp[count][1]:
                        edgeTemp[count][3] = int(edgeTemp[count][3]) + int(com2[int(row[4])][2])
                        if int(edgeTemp[count][3]) > int(edgeTemp[count][2]):
                            #print(int(com2[int(row[4])][2]))
                            #print(elem[incr] + " " + elem[incr+1])
                            solT = True
                            print("sforato")
                            break
                if solT == True:
                    inc = inc+1
                    if inc != row_count:
                        edgeTemp = [x[:] for x in edge]
                    break
            if solT == False or inc == row_count:
                with open('./solve1/05_giorno_solution2.csv', 'a+', newline='') as fSolution:
                    fSolution.write("Commodities numero: " + str(row[4]) + "\n")
                    resPath = csv.writer(fSolution, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    resPath.writerow(elem)
                    edge = [x[:] for x in edgeTemp]
                break
            #print(elem)


costo = 0
for each in edge:
    if int(each[3]) < int(each[2])*0.8:
        pass
    elif int(each[3]) < int(each[2]):
        costo = (each[3]/int(each[2]))*10+costo
        print(costo)
    elif int(each[3]) < int(each[2])*2.2:
        costo = (int(each[3])/int(each[2]))*100+costo
        print(costo)
    elif int(each[3]) < int(each[2])*3:
        costo = (each[3]/int(each[2]))*1000+costo
        print(each)
    else:
        costo = (each[3]/int(each[2]))*10000+costo
        print(each)

print("costo: " + str(costo))
