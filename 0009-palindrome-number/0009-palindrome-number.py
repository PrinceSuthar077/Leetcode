class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        s = str(x)
        a = s[::-1]
        m = int(a)

        if m == x:
            return True
        return False