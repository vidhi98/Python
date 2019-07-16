def eq(a,N):
    for j in range(N):
        arr=a
        n=N
        left_sum=0
        right_sum=0
        k=0
        for k in range(j):
            left_sum += arr[k]
        for k in range (j+1,n):
            right_sum += arr[k]
        if left_sum == right_sum:
            return(j+1)
        
    return(-1)

T=int(input())
for i in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    print(eq(a,N))


            
            
        
    
