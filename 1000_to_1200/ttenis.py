# Question Link: https://www.codechef.com/problems/TTENIS

# cook your dish here
for _ in range(int(input())):
    s = input().strip()
    chef = 0
    opponent = 0
    for ch in s:
        if ch == '1':
            chef += 1
        else:
            opponent += 1
        if (chef >= 11 or opponent >= 11) and abs(chef - opponent) >= 2:
            break
    if chef > opponent:
        print("WIN")
    else:
        print("LOSE")