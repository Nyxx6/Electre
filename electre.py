import numpy as np
# load matrix from file
def Matrix(file):
    return np.loadtxt(file,)
def Critere(n):
    i=0
    C=[]
    while(i<n):
        print("Nom du Critere ",i," :", end=" ")
        crt=input()
        if(crt):
            print("Poids de ",crt," :", end=" ")
            pds=input() 
            if(pds != "" and pds != " "):            
                i=i+1
                C.append([crt,pds])
    return C
def printM(M,n,m):
    for i in range(0,n):
        for j in range(0,m):
            print(str("%.3f" %M[i,j])+"\t\t",end="")
        print()
def printC(C,n):
    for i in range(0,n):
        print(str(C[i])+"\t",end="")
    print()
def maxe(a,b):
    if(a>b): return a
    return b
def sumC(C,i,n):
    if(i>n-1):
        return 0
    return int(C[i][1])+sumC(C,i+1,n)
def Solution(D,C,n):
    sc = int(input("Sueil de concordance = "))
    sd = int(input("Sueil de discordance = "))
    sol=' '
    for i in range(0,n):
        for j in range(0,n):
            if(C[i,j]>=sc and D[i,j]<=sd and sol[len(sol)-1] != str(i)):
                sol=sol+str(i)
    return list(sol.removeprefix(" "))    
def Cordances(M,C,m,n):   
    Mc=np.zeros([n,n])
    Md=np.zeros([n,n])
    t=M.max()-M.min()
    s=sumC(C,0,m)
    for i in range(0,n-1):
        ps1=0;ps2=0  
        d1=0;d2=0
        k=i+1
        while(k<n):
            for j in range(0,n-1):
                if(M[i,j]>=M[k,j]):
                    ps1=ps1+int(C[j][1]) 
                    d2=maxe(d2,M[i,j]-M[k,j])      
                if(M[i,j]<=M[k,j]):
                    ps2=ps2+int(C[j][1])
                    d1=maxe(d1,M[k,j]-M[i,j])
            ps1=ps1/s
            ps2=ps2/s        
            Mc[i,k] = ps1
            Mc[k,i] = ps2        
            d1=d1/t
            d2=d2/t     
            Md[i,k] = d1
            Md[k,i] = d2        
            k=k+1 
    print("Matrice de concordance :");printM(Mc,n,n)
    print("Matrice de discordance :");printM(Md,n,n)
    sol=Solution(Md,Mc,n)
    print("les meilleurs alternatives : ",sol,end="")
def Performance(file):
    M=Matrix(file)
    n=M.shape[0]
    m=M.shape[1]
    C=Critere(n-1)
    printC(C,m)
    printM(M,n,m)
    Cordances(M,C,m,n)

Performance("matrix.txt")


