# Question Link: https://www.codechef.com/problems/DIET

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    stored = 0
    fail = 0
    for i in range(n):
        stored += a[i]
        if stored < k:
            fail = i + 1
            break
        stored -= k
    if fail:
        print(f"NO {fail}")
    else:
        print("YES")