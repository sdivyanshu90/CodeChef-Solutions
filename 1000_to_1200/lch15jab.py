# Question Link: https://www.codechef.com/problems/LCH15JAB

# cook your dish here
from collections import Counter

for _ in range(int(input())):    
    input_string = input()
    
    char_count = Counter(input_string)
    
    most_common_char, most_common_count = char_count.most_common(1)[0]
    
    sum_of_other_counts = sum(count for char, count in char_count.items() if char != most_common_char)
    
    if most_common_count == sum_of_other_counts:
        print("YES")
    else:
        print("NO")