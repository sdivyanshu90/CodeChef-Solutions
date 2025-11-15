# Question Link: https://www.codechef.com/problems/ADVANCE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    target = list(range(x, x + 201))
    if y in target:
        print("YES")
    else:
        print("NO")