class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        a1 = []
        a2 = []
        a3 = []

        while i < m:
            a1.append(nums1[i])
            i += 1

        while j < n:
            a2.append(nums2[j])
            j += 1

        a3 = a1 + a2
        a3.sort()

        for i in range(len(a3)):
            nums1[i] = a3[i]