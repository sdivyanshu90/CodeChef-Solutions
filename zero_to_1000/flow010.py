# Question Link: https://www.codechef.com/problems/FLOW010

# cook your dish here
for _ in range(int(input())):
    s = input()
    if s == "B" or s == "b":
        print("BattleShip")
    elif s == "C" or s == "c":
        print("Cruiser")
    elif s == "D" or s == "d":
        print("Destroyer")
    else:
        print("Frigate")