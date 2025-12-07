# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    first_investor = 10 * a
    second_investor = 5 * b
    if first_investor > second_investor:
        print("FIRST")
    elif second_investor > first_investor:
        print("SECOND")
    else:
        print("ANY")