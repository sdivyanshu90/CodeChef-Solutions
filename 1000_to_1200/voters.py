# cook your dish here
from collections import Counter
import sys

input = sys.stdin.read
data = list(map(int, input().split()))

n1, n2, n3 = data[:3]
numbers = data[3:]

freq = Counter(numbers)
result = sorted(x for x, count in freq.items() if count >= 2)

print(len(result))
print(*result, sep="\n")