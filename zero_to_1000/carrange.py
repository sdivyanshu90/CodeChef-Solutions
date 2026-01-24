# cook your dish here
for _ in range(int(input())):
    p, m, v = map(int, input().split())
    eco = m - (p - 1)
    print(eco * v)