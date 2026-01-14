# cook your dish here
for _ in range(int(input())):
    x = int(input())
    direction = ["East", "South", "West", "North"]
    print(direction[x % 4 - 1])