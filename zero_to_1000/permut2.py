# cook your dish here
while True:
    n = int(input())
    if n == 0:
        break
    
    perm = list(map(int, input().split()))
    inv = [0] * n
    
    for i in range(n):
        inv[perm[i]-1] = i+1
    
    if perm == inv:
        print("ambiguous")
    else:
        print("not ambiguous")