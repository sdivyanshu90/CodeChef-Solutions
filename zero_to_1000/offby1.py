# Question Link: https://www.codechef.com/problems/OFFBY1

# cook your dish here
a, b = map(int, input().split())
print(str(a + b) + "1")

# Approach 2
# a, b = map(int, input().split())
# sum_ab = a + b
# result = f"{sum_ab}1"
# print(result)

# Approach 3
# a, b = map(int, input().split())
# sum_ab = a + b
# result = "{}1".format(sum_ab)
# print(result)

# Approach 4
# a, b = map(int, input().split())
# sum_ab = a + b
# result = str.format("{0}1", sum_ab)
# print(result)

# Approach 5
# a, b = map(int, input().split())
# sum_ab = a + b
# result = '%s1' % sum_ab
# print(result)

# Approach 6
# a, b = map(int, input().split())
# sum_ab = a + b
# result = ''.join([str(sum_ab), '1'])
# print(result)

# Approach 7
# a, b = map(int, input().split())
# sum_ab = a + b
# result = str(sum_ab) + chr(49)  # ASCII value of '1 is 49
# print(result)

# Approach 8
# a, b = map(int, input().split())
# sum_ab = a + b
# result = ''.join([f"{sum_ab}", "1"])
# print(result)