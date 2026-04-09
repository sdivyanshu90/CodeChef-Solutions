# cook your dish here
for _ in range(int(input())):
    x = int(input())
    
    power = 1 << (x.bit_length())
    subtract = power - x
    print(0 if subtract == 0 else x - subtract)