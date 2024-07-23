class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for operation in operations:
            if operation in ("++X", "X++"):
                X += 1
            elif operation in ("--X", "X--"):
                X -= 1
        return X
s=Solution()
operations = ["++X", "X++", "--X", "X--"]
print(s.finalValueAfterOperations(operations))

        