# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in a:
        count += (-((-i) // 2))
        
    print(count)