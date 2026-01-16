# cook your dish here
for _ in range(int(input())):
    g1, s1, b1, g2, s2, b2 = map(int, input().split())
    first = g1 + s1 + b1
    second = g2 + s2 + b2
    
    if first > second:
        print(1)
    else:
        print(2)