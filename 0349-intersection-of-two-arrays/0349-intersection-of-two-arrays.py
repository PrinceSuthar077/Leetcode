class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        l1 = list(s1)
        l2 = list(s2)
        l = []

        for i in s1:
            if i in s2:
                l.append(i)

        return l
