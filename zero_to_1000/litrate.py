# Question Link: https://www.codechef.com/problems/LITRATE

# cook your dish here
for _ in range(int(input())):
    l, p = map(int, input().split())
    literacy = ((p / l))
    # print(literacy)
    if literacy >= 0.75:
        print("YES")
    else:
        print("NO")