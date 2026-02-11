# cook your dish here
for _ in range(int(input())):
    s = input()
    vowel = ["A", "E", "I", "O", "U"]
    t = 0
    for char in s:
        if char in vowel:
            t += 1
    if s[1] in vowel and s[3] in vowel and s[5] in vowel and t == 3:
        print("YES")
    else:
        print("NO")