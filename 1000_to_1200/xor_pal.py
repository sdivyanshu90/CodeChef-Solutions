# Question Link: https://www.codechef.com/problems/XOR_PAL

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    if s == s[::-1]:
        print(0)
        next
    else:
        diff = [int(s[i] == s[-(i+1)]) for i in range(len(s)//2)]
        print(-(-diff.count(0)//2))