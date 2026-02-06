# Question Link: https://www.codechef.com/problems/DARLIG

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 0:
        if n % 4 != 0:
            print("On")
        else:
            print("Off")
    else:
        if n % 4 != 0:
            print("Ambiguous")
        else:
            print("On")