# cook your dish here
n, m, k = map(int, input().split())
res = 0

for _ in range(n):
    q = list(map(int, input().split()))
    total_minutes = sum(q[:-1])
    num_questions = q[-1]

    if total_minutes >= m and num_questions <= 10:
        res += 1

print(res)