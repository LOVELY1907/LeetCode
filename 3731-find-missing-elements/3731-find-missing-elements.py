class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set(nums)
        mn = min(nums)
        mx = max(nums)

        ans = []

        for i in range(mn, mx + 1):
            if i not in seen:
                ans.append(i)
        
        return ans