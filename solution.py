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


'''
for row in comm:
    Sk = nx.shortest_path(G, source=(row[0]), target=row[1])
    for incr in range(len(Sk)-1):
        for count in range(len(edge)):
            if Sk[incr] == edge[count][0] and Sk[incr+1] == edge[count][1]:
                for elem in comm:
                    edge[count][3] = edge[count][3] + row[3]
    print(row)

print(edge)
'''