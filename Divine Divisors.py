from math import sqrt
T=int(input())
N=[]
l1, l2 = [], []
for i in range(T):
    inp=int(input())
    N.append(inp)
for j in range(T):
    step = 2 if N[i]%2 else 1
    for i in range(1, int(N[j-1] ** 0.5) + 1):
        if N[j]%i == 0:
            q=N[j]//i    
            l1.append(i) 
            l2.append(q)    
            if l1[-1] == l2[-1]:
                l1.pop()
    l2=(l2[::-1])
    print(*(l1 + l2))
        
