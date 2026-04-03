# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (arr[j] - arr[i]) == (arr[k] - arr[j]) and i < j < k:
                    flag = False
                    
    if flag:
        print("Yes")
    else:
        print("No")