# Question Link: https://www.codechef.com/problems/TSTROBOT

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    s = input()
    
    moves = set()
    moves.add(x)
    for step in s:
        if step == "R":
            x += 1
            
        else:
            x -= 1
        moves.add(x)
            
    print(len(moves))
    # print(moves)