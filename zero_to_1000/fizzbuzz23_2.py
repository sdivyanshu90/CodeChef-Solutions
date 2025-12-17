# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    tot = 5 * b
    print(a // tot + c)