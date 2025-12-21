# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    mini = n * 10
    maxi = n * 12
    
    if mini <= k <= maxi:
        print("YES")
    else:
        print("NO")