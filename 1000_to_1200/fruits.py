# cook your dish here
for _ in range(int(input().strip())):
    apple, orange, gold = map(int, input().split())
    
    diff = 0
    if apple > orange:
        diff = apple - orange
    else:
        diff = orange - apple
        
    diff = diff - gold
    if diff > 0:
        print(diff)
    else:
        print(0)