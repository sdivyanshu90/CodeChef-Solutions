# cook your dish here
for _ in range(int(input())):
    n, x, y, a, b = map(int, input().split())
    petrol = ((n / a) * x)
    diesel = ((n / b) * y)
    if petrol > diesel:
        print("DIESEL")
    elif diesel > petrol:
        print("PETROL")
    else:
        print("ANY")