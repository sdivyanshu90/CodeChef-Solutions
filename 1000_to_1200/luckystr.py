# cook your dish here
k, n = map(int, input().split())
A = [input().strip() for _ in range(k)]
B = [input().strip() for _ in range(n)]

for s in B:
    if len(s) >= 47:
        print("Good")
        continue
    
    is_good = False
    for a in A:
        if a in s:
            is_good = True
            break
    
    if is_good:
        print("Good")
    else:
        print("Bad")