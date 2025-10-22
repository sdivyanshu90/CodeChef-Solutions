# Question Link: https://www.codechef.com/problems/RECSQ

# cook your dish here
length, breadth, side = map(int, input().split())
area_of_rectangle = length * breadth
area_of_square = side * side
if area_of_rectangle == area_of_square:
    print("YES")
else:
    print("NO")