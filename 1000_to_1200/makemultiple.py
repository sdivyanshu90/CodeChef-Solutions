# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if b % a == 0 or a <= (b - a):
        print('YES')
    else:
        print('NO')