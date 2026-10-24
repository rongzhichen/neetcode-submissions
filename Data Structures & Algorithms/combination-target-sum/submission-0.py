class Solution:
    def combinationSum(self, nums, target):
        result = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] <= remaining:
                    path.append(nums[i])
                    dfs(i, remaining - nums[i])
                    path.pop()

        dfs(0, target)
        return result

