import csv

import networkx as nx

#TO DO: Sistemare l'esecuzione del programma. Funzioni e cose varie.

G = nx.DiGraph()
node = []
edge = []
comm = []

#NODI
#Parametro 1: ID nodo
#Parametro 2: Nome nodo
with open('./dati/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_node(row[0], name=row[1])
        node.append(row)

#ARCHI
#Parametro 1: ID nodo sorgente
#Parametro 2: ID nodo destinazione
#Parametro 3: Capacità arco
with open('./dati/05_giorno_topology.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_edge(row[0], row[1], cap=int(row[2]))
        edge.append(row)

#COMMODITIES
#Parametro 1: ID Sorgente
#Parametro 2: ID Destinazione
#Parametro 3: Banda richiesta
#Parametro 4: Priotrità
i = 0
with open('./dati/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = i
        comm.append(row)
        i = i+1

with open('./out2/05_giorno_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        row[4] = i
        comm.append(row)
        i = i+1
