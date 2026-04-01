# Question Link: https://www.codechef.com/problems/ALBS

# cook your dish here
for _ in range(int(input())):
    n = int(input().strip())
    S = input().strip()
    print(sum(S[i] == S[i+1] for i in range(n-1)))