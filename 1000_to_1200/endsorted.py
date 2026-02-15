# Problem: https://www.codechef.com/problems/ENDSORTED

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    pos1 = a.index(1)
    posN = a.index(n)
    
    if pos1 < posN:
        print(pos1 + (n - 1 - posN))
    else:
        print(pos1 + (n - 1 - posN) - 1)