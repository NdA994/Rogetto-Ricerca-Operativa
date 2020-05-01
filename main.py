import csv
import networkx as nx

#TO DO: Controllare che tutti i dati dai file vengano raccolti per bene.
#TO DO: Controllare che il calcolo di Lk sia fatto bene.
#TO DO: Controllare che il calcolo dei simple path sia fatto bene.
#TO DO: Vedere se i punti di articolazione possono aiutare sotto il punto di vista computazionale
#TO DO: Implementazione brutale per individuare tutte le rotte per le commodities senza alcun tipo di controllo sulla banda
#TO DO: Salvataggio dati di precalcolo
#TO DO: Sistemare l'esecuzione del programma. Funzioni e cose varie.

G = nx.DiGraph()
node = []
edge = []
comm = []

#NODI
#Parametro 1: ID nodo
#Parametro 2: Nome nodo
with open('./dati/01_sites.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_node(row[0], name=row[1])
        node.append(row)

#ARCHI
#Parametro 1: ID nodo sorgente
#Parametro 2: ID nodo destinazione
#Parametro 3: Capacità arco
with open('./dati/01_topology.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        G.add_edge(row[0], row[1], cap=int(row[2]))
        edge.append(row)

#COMMODITIES
#Parametro 1: ID Sorgente
#Parametro 2: ID Destinazione
#Parametro 3: Banda richiesta
#Parametro 4: Priotrità
with open('./dati/01_commodities.csv', newline='') as csvfile:
    topology = csv.reader(csvfile, delimiter=' ')
    for row in topology:
        comm.append(row)

#calcolo Lk
for row in comm:
    Lk = nx.shortest_path_length(G, source=(row[0]), target=row[1])
    if int(row[3]) == 1:
        print(Lk)
        print(nx.shortest_path(G, source=(row[0]), target=row[1]))
        for path in nx.all_simple_paths(G, source=(row[0]), target=row[1], cutoff=Lk+1):
            print(path)

    if int(row[3]) == 2:
        print("ERRORE")
    if int(row[3]) == 3:
        print("ERRORE")

#print(len(comm))
