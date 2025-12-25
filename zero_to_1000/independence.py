# cook your dish here
for _ in range(int(input())):
    o, w, g = map(int, input().split())
    maxi = max(o, w, g)
    
    if maxi <= (o + w + g) - maxi + 1:
        print("YES")
    else:
        print("NO")