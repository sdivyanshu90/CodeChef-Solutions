# Question Link: https://www.codechef.com/problems/CRICMATCH

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    max_score = m * 36
    if max_score >= n:
        print("YES")
    else:
        print("NO")