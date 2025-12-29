# Question Link: https://www.codechef.com/problems/KITCHENCOST

class Solution:
    def compute(self, n, x, a, b):
        # write your code here 
        res = 0
        for i in range(n):
            if a[i] >= x:
                res += b[i]
        return res