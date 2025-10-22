#  Question Link: https://www.codechef.com/problems/CWCTH

# cook your dish here
a, b = map(int, input().split())
if 3 * a <= b:
    print("Rain")
else:
    print("Dry")