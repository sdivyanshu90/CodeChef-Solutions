# Question Link: https://www.codechef.com/problems/LOSTWKND

# cook your dish here
for _ in range(int(input())):
    a1, a2, a3, a4, a5, p = map(int, input().split())
    tot = 0
    a = [a1, a2, a3, a4, a5]
    for num in a:
        tot += (num * p)
    hrs = 24*5
    if tot <= hrs:
        print("No")
    else:
        print("Yes")