# Question Link: https://www.codechef.com/problems/P2169

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ""
    for bit in s:
        if bit == "1":
            res += "0"
        else:
            res += "1"
    print(res)