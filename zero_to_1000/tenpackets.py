# Question Link: https://www.codechef.com/problems/TENPACKETS

# cook your dish here
for _ in range(int(input())):
    pack2, pack4 = map(int, input().split())
    print(min(5 * pack2, 1 * pack2 + 2 * pack4, 3 * pack2 + 1 * pack4))