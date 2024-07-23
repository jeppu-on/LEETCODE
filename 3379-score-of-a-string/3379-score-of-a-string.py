class Solution(object):
    def scoreOfString(self, s):
        score=0
        for i in range(len(s)-1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score 
       
if __name__ == "__main__":
    solution = Solution()
    s="hello"
    print(solution.scoreOfString(s))
        