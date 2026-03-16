# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    wins = 0
    need = []
    
    for i in range(n):
        if a[i] > b[i]:
            wins += 1
        else:
            need.append(b[i] - a[i] + 1)
    
    need.sort()
    
    for cost in need:
        if x >= cost:
            x -= cost
            wins += 1
        else:
            break
    
    if wins > n // 2:
        print("YES")
    else:
        print("NO")