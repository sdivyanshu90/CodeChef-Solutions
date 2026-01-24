# Question Link: https://www.codechef.com/problems/CIELRCPT

# cook your dish here
for _ in range(int(input())):
    p = int(input())
    print((p // 2048) + bin(p % 2048).count('1'))