import random

size = int(input())
inputS = [0]
inputF = [0]
len=0

def getInputs():
    cnt = 0
    while cnt<size:
        S = int(input())
        inputS.append(S)
        F = int(input())
        inputF.append(F)
        cnt+=1


def Partition(A,B,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if(A[j]<=x):
            i=i+1
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
            tmp=B[i]
            B[i]=B[j]
            B[j]=tmp
    tmp=A[i+1]
    A[i+1]=A[r]
    A[r]=tmp
    tmp=B[i+1]
    B[i+1]=B[r]
    B[r]=tmp        
    return i+1

def Randomized_Partion(A,B,p,r):
    i=random.randint(p,r)
    tmp=A[i]
    A[i]=A[r]
    A[r]=tmp
    tmp=B[i]
    B[i]=B[r]
    B[r]=tmp
    return Partition(A,B,p,r)

def Randomized_Quicksort(A,B,p,r):
    if(p<r):
        q=Randomized_Partion(A,B,p,r)
        Randomized_Quicksort(A,B,p,q-1)
        Randomized_Quicksort(A,B,q+1,r)

def Recursive_Activity_Selector(s,f,k,n):
    m=k+1
    while((m<=n) and (s[m]<f[k])):
        m=m+1
    if(m<=n):
        global len
        len=len+1
        output.append(s[m])
        output.append(f[m])
        return Recursive_Activity_Selector(s,f,m,n)
    else:
        return []  
 
output=[]
getInputs()
Randomized_Quicksort(inputF,inputS,0,size)
print(inputF)
Recursive_Activity_Selector(inputS,inputF,0,size)
print(len)
for i in range(0,len*2):
    print(output[i])