# Question Link: https://www.codechef.com/problems/GIFTSRC

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    x, y = 0, 0
    prev_axis = None
    
    for direction in s:
        if direction in "LR":
            axis = 'X'
        else:
            axis = 'Y'
        
        if axis == prev_axis:
            continue
        
        if direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        elif direction == "U":
            y += 1
        else:
            y -= 1
        
        prev_axis = axis
    
    print(x, y)