# Question Link: https://www.codechef.com/problems/ADJSUMPAR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    zeros, ones = 0, 0
    for bit in b:
        if bit == 0:
            zeros += 1
        else:
            ones += 1
    
    if ones % 2 == 0:
        print("YES")
    else:
        print("NO")