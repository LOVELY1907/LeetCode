class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum1 = 0
        product = 1
        while temp>0:
            r = temp % 10
            temp//=10
            sum1+=r
            product*=r
        return product - sum1