# Question Link: https://www.codechef.com/problems/TRAINEVOD

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd, even = 0, 0

    for i in range(n):
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
            
    print(max(odd, even))