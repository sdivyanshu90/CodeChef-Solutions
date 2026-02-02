# cook your dish here
for _ in range(int(input())):
    r1, w1, c1 = map(int, input().split())
    r2, w2, c2 = map(int, input().split())
    
    if (r1 > r2 and w1 > w2 and c1 > c2) or (r1 > r2 and w1 > w2) or (r1 > r2 and c1 > c2) or (w1 > w2 and c1 > c2):
        print("A")
    else:
        print("B")