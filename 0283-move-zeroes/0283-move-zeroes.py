class Solution:
    def moveZeroes(self, nums):

        k = 0

        for num in nums:

            if num != 0:
                nums[k] = num
                k += 1

        while k < len(nums):
            nums[k] = 0
            k += 1