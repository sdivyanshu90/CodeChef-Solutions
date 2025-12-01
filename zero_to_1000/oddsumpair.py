class Solution:
    def check_odd_pairs(self, a, b, c):
        # write your code here
        # cook your dish here
        if (a + b) % 2 != 0 or (b + c) % 2 != 0 or (a + c) % 2 != 0:
            return "YES"
        else:
            return "NO"