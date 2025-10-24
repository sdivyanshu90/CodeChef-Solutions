# Question Link: https://www.codechef.com/problems/INCAT

# cook your dish here
s = input().strip()

c_count = a_count = t_count = 0
for char in s:
    if char == 'c':
        c_count += 1
    elif char == 'a':
        a_count += 1
    elif char == 't':
        t_count += 1

if c_count == 1 and a_count == 1 and t_count == 1:
    print("Yes")
else:
    print("No")


# Approach 2: Using Stack
# cook your dish here
s = input().strip()
stack = ["c", "a", "t"]

for char in s:
    if char in stack:
        stack.remove(char)
        
if len(stack) == 0:
    print("Yes")
else:
    print("No")