class Solution(object):
    def isHappy(self, n):
        l = []

        while n != 1:
            s = 0

            while n > 0:
                r = n % 10
                s = s + r * r
                n = n // 10

            n = s

            if n in l:
                return False

            l.append(n)

        return True