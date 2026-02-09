# Question Link: https://www.codechef.com/problems/EZSPEAK

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = 0
    temp = 0
    for char in s:
        
        if char not in vowel:
            temp += 1
        else:
            temp = 0
        consonant = max(temp, consonant)
    if consonant >= 4:
        print("NO")
    else:
        print("YES")