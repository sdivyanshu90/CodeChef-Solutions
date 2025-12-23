# cook your dish here
for _ in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    
    r = C.count(1)
    b = C.count(2)
    undecided = C.count(0)
    diff = abs(r - b)
    
    if diff <= undecided and (undecided - diff) % 2 == 0:
        print("YES")
    else:
        print("NO")