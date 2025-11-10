# Question Link: https://www.codechef.com/problems/TCKTFINE

# cook your dish here
for _ in range(int(input())):
    p, q, r = map(int, input().split())
    print(p * (q - r))