class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for i in stones:
            if i in jewels:
                c=c+1
        return c
jewels="aA"
stones="aAAbbbb"
s=Solution()
x=s.numJewelsInStones(jewels, stones)
print(x)
        