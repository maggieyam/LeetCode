class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        num = int(sqrt(n))
        for i in range(2, num + 1):
            square = i * i
            for j in range(square, n + 1):
                if j == square:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j - square] + dp[square]) 
                
        return dp[-1]
            