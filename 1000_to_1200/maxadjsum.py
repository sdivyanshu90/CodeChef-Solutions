# Question Link: https://www.codechef.com/problems/MAXADJSUM

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    total = sum(a)
    answer = 2 * total - a[0] - a[1]
    print(answer)