# Question Link: https://www.codechef.com/problems/WOLFDOWN

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    idx = s.find("1")
    # print(idx)
    if idx == -1:
        print(len(s))
    else:
        print(idx)