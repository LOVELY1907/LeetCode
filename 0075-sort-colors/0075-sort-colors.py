class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red,white,blue =0,0,0
        for i in range(len(nums)):
            val = nums[i]
      
            nums[blue]=2
            blue+=1

            if val<2:
                nums[white]=1
                white+=1
            
            if val==0:
                nums[red]=0
                red+=1
        