# Question Link: https://www.codechef.com/problems/PBREV

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for num in a:
        if num > 4:
            count += 1
    if count == n:
        print("YES")
    else:
        print("NO")