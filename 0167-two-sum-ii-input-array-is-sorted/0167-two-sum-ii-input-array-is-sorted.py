class Solution:
    def twoSum(self, arr, t):
        l = 0
        r = len(arr) - 1

        while l < r:
            total = arr[l] + arr[r]

            if total == t:
                return [l + 1, r + 1]

            if total < t:
                l = l + 1

            if total > t:
                r = r - 1