import csv
import os
import networkx as nx

G = nx.DiGraph()
node = []
edge = []
comm = []
com2 = []
pres = []

# ARCHI
# Parametro 1: ID commodities
# Parametro 2: N soluzioni
with open('./out2/resPath.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        if int(row[1]) == 1:
            pres.append(row)

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
with open('./dati/05_giorno_topology.csv', newline='') as csvfile:
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
with open('./dati/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = i
        com2.append(row)
        comm.append(row)
        i = i + 1

edge = [row + [0] for row in edge]

if os.path.exists('./preSolve2/05_giorno_solution.txt'):
    print("CANCELLATO ./preSolve2/05_giorno_solution.txt")
    os.remove('./preSolve2/05_giorno_solution.txt')
if os.path.exists('./preSolve2/05_giorno_commodities.csv'):
    print("CANCELLATO ./preSolve2/05_giorno_commodities.csv")
    os.remove('./preSolve2/05_giorno_commodities.csv')
if os.path.exists('./preSolve2/05_giorno_topology.csv'):
    print("CANCELLATO ./preSolve2/05_giorno_topology.csv")
    os.remove('./preSolve2/05_giorno_topology.csv')

for row in pres:
    comm[int(row[0])] = []
comm = [x for x in comm if x != []]

with open('./preSolve2/05_giorno_commodities.csv', 'w', newline='') as csvPath:
    resPath = csv.writer(csvPath, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    for row in comm:
        resPath.writerow(row)

with open('./preSolve2/05_giorno_solution.txt', 'w', newline='') as fSolution:
    for row in pres:
        fSolution.write("Commodities numero: " + row[0] + "\n")
        with open('./out2/' + row[0] + '.csv', newline='') as csvfile:
            route = csv.reader(csvfile, delimiter=' ')
            for path in route:
                fSolution.write(str(path) + "\n")
                for incr in range(len(path)-1):
                    for count in range(len(edge)):
                        if path[incr] == edge[count][0] and path[incr+1] == edge[count][1]:
                            edge[count][3] = edge[count][3] + int(com2[int(row[0])][2])

with open('./preSolve2/05_giorno_topology.csv', 'w', newline='') as csvPath:
    resPath = csv.writer(csvPath, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    for row in edge:
        resPath.writerow(row)

