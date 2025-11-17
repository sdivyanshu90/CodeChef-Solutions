# Question Link: https://www.codechef.com/problems/CMASKS

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if 100 * x >= 10 * y:
        print("Cloth")
    else:
        print("Disposable")