# Question Link: https://www.codechef.com/problems/MAKESUB

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    idx = []
    for i in range(n):
        if s[i] == "1":
            idx.append(i)
    # print(idx)
    res = 0
    if len(idx) > 1:
        mini = idx[0]
        maxi = idx[-1]
        for i in range(mini, maxi + 1):
            if i in idx:
                continue
            else:
                res += 1
        print(res)
    else:
        print(res)