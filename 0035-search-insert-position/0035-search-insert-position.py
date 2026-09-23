class Solution:
    def searchInsert(self, arr, ins):
        l = 0
        h = len(arr) - 1

        while l <= h:
            mid = l + (h - l) // 2

            if arr[mid] == ins:
                return mid

            elif arr[mid] < ins:
                l = mid + 1

            else:
                h = mid - 1

        return l