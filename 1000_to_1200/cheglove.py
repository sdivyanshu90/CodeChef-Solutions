# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    g = list(map(int, input().split()))
    
    front = True
    back = True
    
    for i in range(n):
        if l[i] > g[i]:
            front = False
        if l[i] > g[n - 1 - i]:
            back = False
    
    if front and back:
        print("both")
    elif front:
        print("front")
    elif back:
        print("back")
    else:
        print("none")