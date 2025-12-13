# Question Link: https://www.codechef.com/problems/CHESSDIST

# cook your dish here
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(max(abs(x2 - x1), abs(y2 - y1)))