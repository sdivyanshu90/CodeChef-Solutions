# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if n % 2 == 0:
        rows = n // 2
    else:
        rows = (n // 2) + 1
        
    if m % 2 == 0:
        seats = m // 2
    else:
        seats = (m // 2) + 1
        
    print(rows * seats)