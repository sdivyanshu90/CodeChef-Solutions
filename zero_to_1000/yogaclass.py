# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    type1 = ((n // 2) * y + ((n % 2) * x))
    type2 = n * x
    print(max(type1 , type2))