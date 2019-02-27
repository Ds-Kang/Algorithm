import heapq


class Node(object):
    left = None
    right = None
    key= None
    weight = 0

    def __init__(self, k, w):
        self.key =k
        self.weight = w

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    def __cmp__(self, a):
        return cmp(self.weight, a.weight)


def getInputs():
    cnt = 0
    while cnt<size:
        S = int(input())
        table.append([cnt,S])
        cnt+=1

def Huffman(C):
    Q=[Node(x,weight) for x,weight in C]
    heapq.heapify(Q)
    for i in range(1,size):
        L=heapq.heappop(Q)
        R=heapq.heappop(Q)
        z=Node(None,L.weight+R.weight)
        z.setChildren(L,R)
        heapq.heappush(Q,z)
    return heapq.heappop(Q)

def Codeit(s,node,key):
    if node.key!=None:
        if node.key==key:
            print (s)
    else:
        Codeit(s+'0',node.left,key)
        Codeit(s+'1',node.right,key)

size=int(input())
table=[]
getInputs()
huff=Huffman(table)
for i in range(0,size):
    Codeit('',huff,i)