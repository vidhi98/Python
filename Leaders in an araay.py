T=int(input())
for j in range(T):
    arr=[]
    result=[]
    n=int(input())
    arr = list(map(int,input().split()))
    max=arr[n-1]
    result.append(max)
    for i in range(n-2,-1,-1):
        if arr[i]>max:
            result.append(arr[i])
            max=arr[i]
    result.reverse()
    print(*result)        
        
        
