# Question Link: https://www.codechef.com/problems/C00K0FF

# cook your dish here
difficulty_map = {
    'cakewalk': 1,
    'easy': 2,
    'simple': 3,
    'easy-medium': 4,
    'medium': 4,
    'medium-hard': 5,
    'hard': 5
}

for _ in range(int(input())):
    difficulty_set = set()
    for _ in range(int(input())):
        s = input().strip()
        difficulty_set.add(difficulty_map.get(s, 0))
    
    if difficulty_set == {1, 2, 3, 4, 5}:
        print('Yes')
    else:
        print('No')