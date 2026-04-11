# Question Link: https://www.codechef.com/problems/TRACE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0

    for i in range(n):
        diag_sum = sum(m[j + i][j] for j in range(n - i))
        max_sum = max(max_sum, diag_sum)

    for j in range(1, n):
        diag_sum = sum(m[i][i + j] for i in range(n - j))
        max_sum = max(max_sum, diag_sum)

    print(max_sum)