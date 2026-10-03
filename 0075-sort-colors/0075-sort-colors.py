class Solution:
    def sortColors(self, nums):
        count0 = nums.count(0)
        count1 = nums.count(1)

        for i in range(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i < count0 + count1:
                nums[i] = 1
            else:
                nums[i] = 2