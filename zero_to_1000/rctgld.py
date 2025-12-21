# Question Link: https://www.codechef.com/problems/RCTGLD

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    width = (n // 4)
    length = (n - (2 * width)) // 2
    print(width * length)

# Approach 2
# for _ in range(int(input())):
#     n = int(input())
#     max_area = 0
#     for w in range(1, n//2):
#         l = (n - 2*w) // 2
#         area = w * l
#         if area > max_area:
#             max_area = area
#     print(max_area)