# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    sunny, rainy = 0, 0
    for num in a:
        if num == 1:
            sunny += 1
        else:
            rainy += 1
            
    if sunny > rainy:
        print("YES")
    else:
        print("NO")