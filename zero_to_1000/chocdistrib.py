# cook your dish here
for _ in range(int(input())):
    n = int(input())
    mini = 1
    maxi = n
    if n % 2 != 0:
        mini = n // 2 + 1
    else:
        mini = n // 2
    print(mini, maxi)