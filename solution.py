import csv
import networkx as nx

G = nx.DiGraph()
node = []
edge = []
comm = []

# NODI
# Parametro 1: ID nodo
# Parametro 2: Nome nodo
with open('./dati/01_sites.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_node(row[0], name=row[1])
        node.append(row)
costo = 300
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
i = 0
with open('./dati/01_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = i
        comm.append(row)
        i = i + 1

#print(len(comm))
edge = [row + [0] for row in edge]

print(comm)

for row in comm:
    print(row[4])
    with open('./out1/'+str(row[4])+'.csv', newline='') as csvfile:
        path = csv.reader(csvfile, delimiter=' ')
        for elem in path:
            print(elem)
            for incr in range(len(elem)-1):
                for count in range(len(edge)):
                    if elem[incr] == edge[count][0] and elem[incr+1] == edge[count][1]:
                        edge[count][3] = int(edge[count][3]) + int(comm[int(row[4])][2])
                        print(comm[int(row[4])][2])
                        if int(edge[count][3]) > int(edge[count][2]):
                            print("sforato")
            break



for each in edge:
    if each[3] < int(each[2])*0.8:
        pass
    elif each[3] < int(each[2]):
        costo = each[3]/int(each[2])+costo
    elif each[3] < int(each[2])*2.2:
        costo = each[3]/int(each[2])+costo
    elif each[3] < int(each[2])*3:
        costo = each[3]/int(each[2])+costo

print("costo: " + str(costo))

