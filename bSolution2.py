import csv
import networkx as nx

G = nx.DiGraph()
lEdg = []
node = []
edge = []
comm = []
com2 = []

# NODI
# Parametro 1: ID nodo
# Parametro 2: Nome nodo
with open('./dati/05_giorno_sites.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_node(row[0], name=row[1])
        node.append(row)

# ARCHI
# Parametro 1: ID nodo sorgente
# Parametro 2: ID nodo destinazione
# Parametro 3: Capacità arco
with open('./preSolve2/05_giorno_topology.csv', newline='') as csvfile:
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
with open('./preSolve2/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        comm.append(row)

j = 0
with open('./dati/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = j
        com2.append(row)
        j = j+1

edge = [row + [0] for row in edge]

i = 0
for row in edge:
    row[4] = i
    i = i+1

for row in comm:
    print(row[4])
    with open('./out2/'+str(row[4])+'.csv', newline='') as csvfile:
        path = csv.reader(csvfile, delimiter=' ')
        for elem in path:
            for incr in range(len(elem)-1):
                for count in range(len(edge)):
                    if elem[incr] == edge[count][0] and elem[incr+1] == edge[count][1]:
                        edge[count][3] = int(edge[count][3]) + int(com2[int(row[4])][2])
            break

costo = 0
for each in edge:
    if int(each[3]) < int(each[2])*0.8:
        pass
    elif int(each[3]) < int(each[2]):
        costo = (each[3]/int(each[2]))*10+costo
        print(costo)
    elif int(each[3]) < int(each[2])*2.2:
        costo = (each[3]/int(each[2]))*100+costo
        print(costo)
    elif int(each[3]) < int(each[2])*3:
        costo = (each[3]/int(each[2]))*1000+costo
        print(costo)
    else:
        costo = (each[3]/int(each[2]))*10000+costo

print("costo: " + str(costo))
