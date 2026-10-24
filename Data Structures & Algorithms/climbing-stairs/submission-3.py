class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return(1)
        memo = {0:1, 1:1}
        def ways(steps):
            if steps in memo:
                return memo[steps]

            memo[steps] = ways(steps - 1) + ways(steps - 2)
            return memo[steps]

        return(ways(n-2)+ways(n-1))
        