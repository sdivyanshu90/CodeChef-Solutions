# cook your dish here
for _ in range(int(input())):
    x = int(input())
    output = 100 - round(x/10)*10 if x%10 != 5 else 100 - round((x+1)/10)*10
    print(output)