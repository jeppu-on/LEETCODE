class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")

address="1.1.1.1"
s=Solution()
x=s.defangIPaddr(address)
print(x)
        
        