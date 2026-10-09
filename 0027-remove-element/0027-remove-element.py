class Solution(object):
    def removeElement(self, nums, val):
        l = []

        for i in nums:
            if i != val:
                l.append(i)

        n = len(l)
        nums[:n] = l

        return n