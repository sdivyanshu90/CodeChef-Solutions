# Question Link: https://www.codechef.com/problems/MAX_BIN

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    
    if s[0] != "1":
        s[0] = "1"
        k -= 1
    s.append("0" * k)
    print("".join(s))