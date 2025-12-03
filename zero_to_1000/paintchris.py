# Question Link: https://www.codechef.com/problems/PAINTCHRIS

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    area = x * y
    print((z // 2) // area)