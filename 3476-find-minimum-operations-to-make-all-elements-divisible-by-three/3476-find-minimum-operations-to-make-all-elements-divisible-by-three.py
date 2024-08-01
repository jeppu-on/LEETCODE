class Solution(object):
    def minimumOperations(self, nums):
        c=0
        for i in nums:
            if i%3==1:
                c=c+1
            elif i%3==2:
                c=c+1
        return c
nums=[]
s=Solution()
x=s.minimumOperations(nums)
print(x)               
        