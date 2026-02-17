# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    ones = s.count("1")
    rem = 120 - n
    percent = (ones + rem) / 120
    # print(percent)
    if percent * 100 >= 75:
        print("YES")
    else:
        print("NO")