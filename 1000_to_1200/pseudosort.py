# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    idx = -1
    
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            count += 1
            idx = i
    
    if count == 0:
        print("YES")
    elif count == 1:
        a[idx], a[idx + 1] = a[idx + 1], a[idx]
        
        if all(a[i] <= a[i + 1] for i in range(n - 1)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")