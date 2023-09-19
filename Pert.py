import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

options = {
    'node_color': 'turquoise',
    'node_size': 1000,
    'width': 5,
}
i=0
ls=[]
print("")

des=input("Número de actividades : ")
de=int(des)

if i <= de:
    H = nx.path_graph(de+1)
    G.add_nodes_from(H)
    
for i in range(de):
    #print(i+1)
    ls.append(i+1)

print(ls)

z=0
w=0

def pre2():
    w=int(input(f"de quien mas precede la actividad {x+1} : "))
    G.add_edge(w,ls[x])


for x in range(de-1): 
    z=int(input(f"Cual es la precedencia de la Actividad {x+1}: "))
    if z <= de:
        G.add_edge(z,ls[x])
        opc=int(input("Tiene otra Precedencia: \n1.Si 2.No : "))
        if opc==1:
            pre2()
            opc=int(input("Tiene otra Precedencia: \n1.Si 2.No : "))
            if opc==1:
                pre2()
                continue
            elif opc==2:
                continue

nx.draw(G, with_labels=True, **options)
plt.show()
