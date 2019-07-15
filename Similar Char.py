import collections
D = collections.Counter('abcdefghijklmnopqrstuvwxyz')
N = int(input())
S = input()
Q = int(input())
P = []
result=[]
for i in range(Q):
    inp=int(input())
    P.append(inp)
for j in S:
     D[j]+=1
     result.append(D[j]-1)
for j in range(Q):
     print(result[P[j]-1]-1)
           
