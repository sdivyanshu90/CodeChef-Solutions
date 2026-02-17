# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    twos = 0
    for num in a:
        if num == 2:
            twos += 1
            
    if twos % 8 == 0:
        print("YES")
    else:
        print("NO")