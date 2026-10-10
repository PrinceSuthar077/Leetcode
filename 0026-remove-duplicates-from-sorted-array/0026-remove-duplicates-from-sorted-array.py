class Solution(object):
    def removeDuplicates(self, nums):
        s = sorted(set(nums))
        l = len(s)
        nums[:l] = s
        return l