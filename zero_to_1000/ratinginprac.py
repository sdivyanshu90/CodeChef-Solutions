# Question Link: https://www.codechef.com/problems/RATINGINPRAC

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = True
    for i in range(n - 1):
        if a[i + 1] >= a[i]:
            continue
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")