# Question Link: https://www.codechef.com/problems/FINDK3

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    
    possible_pairs = [
        (x * y, z),
        (x * z, y),
        (y * z, x),
    ]
    
    found = False
    for a, b in possible_pairs:
        if a % b == 0:
            print(a, b)
            found = True
            break
    
    if not found:
        print(-1)