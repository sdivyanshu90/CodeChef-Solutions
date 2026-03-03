# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    zeros = s.count("0")
    ones = s.count("1")
    
    if zeros == n or ones == n:
        print(n)
    else:
        print(1)