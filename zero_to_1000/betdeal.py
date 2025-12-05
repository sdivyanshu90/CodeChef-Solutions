# Question Link: https://www.codechef.com/problems/BETDEAL

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    first = 100 - a
    second = 200 - round(200 * (b/100))
    if first < second:
        print("FIRST")
    elif second < first:
        print("SECOND")
    else:
        print("BOTH")