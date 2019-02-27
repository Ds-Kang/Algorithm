class Graph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.w = {}

    def add_edge(self,from_node,to_node,weight):
        for x in G.nodes:
            if x.name==from_node:
                v=x
        v.adj.append(to_node)
        self.w[(from_node,to_node)]=weight

class node:
    d=0
    pi=None

    def __init__(self,name):
        self.name=name
        self.adj=[]

class Heap:
    def __init__(self,list):
        self.heapsize= len(list)
        self.list=list

    def build(self):
        for i in range(int(len(self.list)/2),0,-1):
            Heap.min_heapify(self,i)

    def min_heapify(self,i):
        l= left(i)
        r= right(i)
        if l<=self.heapsize and (self.list[l-1].d < self.list[i-1].d or (self.list[l-1].d == self.list[i-1].d and self.list[l-1].name < self.list[i-1].name)):
            min=l
        else:
            min=i
        if r<=self.heapsize and (self.list[r-1].d < self.list[min-1].d or (self.list[r-1].d == self.list[min-1].d and self.list[r-1].name < self.list[min-1].name)):
            min= r
        if min!=i:
            tmp = self.list[i-1]
            self.list[i-1]=self.list[min-1]
            self.list[min-1]=tmp
            Heap.min_heapify(self,min)

    def extract_min(self):
        min=self.list[0]
        self.list[0]=self.list[self.heapsize-1]
        self.list.remove(self.list[self.heapsize-1])
        self.heapsize=self.heapsize-1
        Heap.min_heapify(self,1)
        return min

def right(i):
    return 2*i+1

def left(i):
    return 2*i

def parent(i):
    return i/2



def Dijkstra(G,s):
    ISS(G,s)
    Q=Heap([G.nodes[Names] for Names in range(0,len(G.nodes))])
    while(Q.list):
        Heap.build(Q)
        u=Heap.extract_min(Q)
        if u.adj==None:
            continue
        for V in u.adj:
            for x in G.nodes:
                if x.name==V:
                    v=x
            Relax(u,v,G.w[(u.name,v.name)])

def Relax(u,v,w):
    if v.d > u.d +w:
        v.d = u.d +w
        v.pi = u

def ISS(G,s):
    for v in G.nodes:
        v.d=float('inf')
        v.pi=None
    s.d=0

N=raw_input().split(',')
Ns=[]
for i in range(0,len(N)):
    Ns.append(node(N[i]))
G=Graph(Ns)

length=int(input())
for i in range(0,length):
    edge=raw_input().split(',')
    G.add_edge(edge[0],edge[1],int(edge[2]))

Dijkstra(G,G.nodes[0])
for i in range(0,len(Ns)):
    print(G.nodes[i].d)