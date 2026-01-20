# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    team1 = sum(a[i] for i in range(len(a)) if i % 2 == 0)
    team2 = sum(a[i] for i in range(len(a)) if i % 2 != 0)
    
    if team1 > team2:
        print(1)
    elif team2 > team1:
        print(2)
    else:
        print(0)