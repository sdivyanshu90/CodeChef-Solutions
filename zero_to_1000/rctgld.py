# cook your dish here
for _ in range(int(input())):
    n = int(input())
    width = (n // 4)
    length = (n - (2 * width)) // 2
    print(width * length)