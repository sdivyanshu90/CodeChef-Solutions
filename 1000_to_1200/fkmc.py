# Question Link: https://www.codechef.com/problems/FKMC

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    zero = 0
    maxi = 0
    ones = s.count("1")
    for num in s:
        if num == "0":
            zero += 1
        else:
            zero = 0
        maxi = max(zero, maxi)
    print(maxi + ones)