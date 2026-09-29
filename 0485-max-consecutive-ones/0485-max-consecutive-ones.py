class Solution:
    def findMaxConsecutiveOnes(self, nums):
        c1 = 0
        cmax = 0

        for i in nums:
            if i == 1:
                c1 = c1 + 1
                if c1 > cmax:
                    cmax = c1
            if i == 0:
                c1 = 0
        return cmax      