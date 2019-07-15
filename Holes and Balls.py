N = int(input())
DH = list(map(int,input().split()))
M = int(input())
DB = list(map(int,input().split()))
hd = ['']*(N)
result=[]
for i in range(N):
    hd[i] = i+1
for i in range(M):
    ball=False
    for j in range(N-1,-1,-1):
        if DB[i] <= DH[j]:
            if hd[j]>0:
                hd[j]-=1
                result.append(j+1)
                ball=True
                break
    if ball==False:
        result.append(0)
print(*result)
