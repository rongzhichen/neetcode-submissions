class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        for col in range(n + 1):
            memo[0][col] = 0

        for row in range(m + 1):
            memo[row][0] = 0

        memo[1][1] = 1  # The actual starting cell

        def dp(row, col):
            if memo[row][col] != -1:
                return memo[row][col]

            memo[row][col] = (
                dp(row - 1, col)
                + dp(row, col - 1)
            )
            return memo[row][col]

        return dp(m, n)