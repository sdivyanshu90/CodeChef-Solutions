# Question Link: https://www.codechef.com/problems/FLOW007

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    num = ""
    while n != 0:
        num += str(n % 10)
        n = n // 10
    print(int(num))