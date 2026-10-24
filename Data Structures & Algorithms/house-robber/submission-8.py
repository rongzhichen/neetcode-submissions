class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return(nums[0])
        if len(nums) ==2:
            return(max(nums[0], nums[1]))
        memo = {0:nums[0], 1:nums[1], 2: max(nums[0]+nums[2], nums[1])}
        def dp(num):
            if num in memo:
                return(memo[num])
            memo[num] = max(dp(num-2)+nums[num], dp(num-1), dp(num-3)+nums[num])
            return(memo[num])
        return(max(dp(len(nums)-1), dp(len(nums)-2)))
            

        

        