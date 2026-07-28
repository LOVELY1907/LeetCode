class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in nums:
            c = 0 # count initialized to zero for all values in array
            for j in nums:
                if j < i:
                    c += 1 # increase count if j<i (1<8)
            ans.append(c)

        return ans