class Solution(object):
    def buildArray(self, nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
nums=[]
s=Solution()
x=s.buildArray(nums)
print(x)
        