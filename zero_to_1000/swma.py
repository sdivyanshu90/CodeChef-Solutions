# cook your dish here
for _ in range(int(input())):
    a, b = map(str, input().split())
    if a[::-1] > b or a > b or a > b[::-1] or a[::-1] > b[::-1]:
        print("Yes")
    else:
        print("No")