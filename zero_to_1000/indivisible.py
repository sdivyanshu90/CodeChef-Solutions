# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    
    for i in range(2, 100):
        if a % i != 0 and b % i != 0 and c % i != 0:
            print(i)
            break