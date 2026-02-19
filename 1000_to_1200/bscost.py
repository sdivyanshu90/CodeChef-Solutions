# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    s = input().strip()
    
    c0 = s.count('0')
    c1 = s.count('1')
    
    if c0 == 0 or c1 == 0:
        print(0)
    else:
        print(min(x, y))