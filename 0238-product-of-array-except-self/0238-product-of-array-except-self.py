class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        result = [0] * n

        # Build prefix products
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix products
        suffix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Combine prefix and suffix
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result