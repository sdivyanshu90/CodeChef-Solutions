# Question Link: https://www.codechef.com/problems/COMM3

# cook your dish here
for _ in range(int(input())):
    R = int(input())
    
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    def dist_sq(xa, ya, xb, yb):
        return (xa - xb)**2 + (ya - yb)**2
    
    count = 0
    
    if dist_sq(x1, y1, x2, y2) <= R * R:
        count += 1
        
    if dist_sq(x1, y1, x3, y3) <= R * R:
        count += 1
        
    if dist_sq(x2, y2, x3, y3) <= R * R:
        count += 1
    
    if count >= 2:
        print("yes")
    else:
        print("no")