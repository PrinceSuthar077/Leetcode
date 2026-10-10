class Solution(object):
    def removeDuplicates(self, nums):
        s = sorted(set(nums))
        n = len(s)
        nums[:n] = s
        return n