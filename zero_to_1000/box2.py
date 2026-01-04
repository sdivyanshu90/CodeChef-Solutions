# cook your dish here
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    diff = abs(x - y)
    
    if diff == k:
        print(0)
    elif k > (x + y):
        print(-1)
    elif (k - diff) % 2 != 0:
        print(-1)
    else:
        print(abs(k - diff) // 2)