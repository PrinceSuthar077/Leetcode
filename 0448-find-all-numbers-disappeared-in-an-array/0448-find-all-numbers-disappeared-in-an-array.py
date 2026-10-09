class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        r = []
        s = set(nums)

        for i in range(1, n + 1):
            if i not in s:
                r.append(i)

        return r