T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    right_sumsum=0
    flag=0
    right_sum = sum(arr)
    left_sum = 0
    result = []
    for j in range(n):
        right_sum = right_sum - arr[j]
        if left_sum == right_sum:
            result.append(j+1)
            flag +=1
        left_sum += arr[j]
    print(*result)
    if flag == 0:
        print(-1)
        
        
        
        
