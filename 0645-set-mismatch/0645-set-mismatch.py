class Solution:
    def findErrorNums(self, nums):
        s = []
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                s.append(nums[i])

        for i in range(1, len(nums) + 1):
            if i not in nums:
                s.append(i)

        return s