
class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []

        for i in range(left, right + 1):
            n = i
            valid = True

            while n > 0:
                digit = n % 10

                if digit == 0 or i % digit != 0:
                    valid = False
                    break

                n = n // 10

            if valid:
                result.append(i)

        return result
